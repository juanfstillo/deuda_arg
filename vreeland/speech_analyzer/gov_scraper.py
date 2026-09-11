from __future__ import annotations

import csv
import hashlib
import re
import time
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Dict, Iterator, Optional, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

"""Scrapers for the three government sources feeding Track 1.

Selectors here were derived by fetching and inspecting real pages, not
guessed:

- casarosada.gob.ar/informacion/{discursos,conferencias}: Joomla listing,
  each entry is `div.item > a[href] > time` (Spanish date text) +
  `.category-item-title h3`. Individual pages expose the body as `<p>` tags
  inside `article`/`div.item-page`; the first `<p>` duplicates the page
  title and is dropped.
- argentina.gob.ar/economia/noticias: Drupal listing, `a.panel.panel-default`
  with a machine-readable `<time datetime="YYYY-MM-DD ...">`, paginated via
  `?page=N` (0-indexed). Article body lives in `div.panel-pane.pane-texto`.

robots.txt: casarosada.gob.ar publishes no crawl-delay (Joomla default file)
but is rate-limited here anyway out of courtesy. argentina.gob.ar's
robots.txt explicitly states `Crawl-delay: 10` for all user agents — that is
respected exactly, not treated as a suggestion.
"""

USER_AGENT = "Mozilla/5.0 (compatible; UBA-research-bot/1.0; contact: juan.stillo1@gmail.com)"

CASAROSADA_BASE = "https://www.casarosada.gob.ar"
ECONOMIA_NOTICIAS_URL = "https://www.argentina.gob.ar/economia/noticias"

MILEI_INAUGURATION = date(2023, 12, 10)

_MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "setiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12,
}


def _short_entry_id(raw: str, max_len: int = 60) -> str:
    """Derive a filesystem-safe, stable id from a URL's last path segment.

    Casarosada slugs carry a leading numeric Joomla content id ("51222-...")
    which is short and already unique — use just that. Slugs with no such
    prefix (argentina.gob.ar noticias) can run past Windows' ~260-char path
    limit on their own (some casarosada titles are long enough that even
    the numeric-id shortcut wouldn't have been needed for them, but noticia
    slugs regularly are), so truncate and disambiguate with a short hash.
    """
    match = re.match(r"^(\d+)-", raw)
    if match:
        return match.group(1)
    if len(raw) <= max_len:
        return raw
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]
    return f"{raw[:max_len]}-{digest}"


def _parse_casarosada_date(text: str) -> Optional[date]:
    """Parse '<Día> DD de <Mes> de YYYY' listing dates (Joomla `<time>` text)."""
    match = re.search(r"(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", text, re.IGNORECASE)
    if not match:
        return None
    day, month_name, year = match.groups()
    month = _MESES.get(month_name.lower())
    if month is None:
        return None
    return date(int(year), month, int(day))


@dataclass
class ListingEntry:
    source_type: str  # "discurso" | "conferencia" | "comunicado_economia"
    entry_id: str
    title: str
    entry_date: date
    url: str


class RateLimiter:
    """Enforces a minimum delay between requests to a given host."""

    def __init__(self, delays: Dict[str, float], default_delay: float = 1.0):
        self.delays = delays
        self.default_delay = default_delay
        self._last_request: Dict[str, float] = {}

    def wait(self, host: str) -> None:
        delay = self.delays.get(host, self.default_delay)
        last = self._last_request.get(host)
        if last is not None:
            remaining = delay - (time.monotonic() - last)
            if remaining > 0:
                time.sleep(remaining)
        self._last_request[host] = time.monotonic()


def _get(session: requests.Session, url: str, rate_limiter: RateLimiter) -> requests.Response:
    host = urlparse(url).netloc
    rate_limiter.wait(host)
    response = session.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    response.encoding = "utf-8"
    return response


def iter_casarosada_section(
    section: str,
    cutoff: date,
    session: requests.Session,
    rate_limiter: RateLimiter,
    max_pages: Optional[int] = None,
) -> Iterator[ListingEntry]:
    """Yield entries from casarosada.gob.ar/informacion/{discursos|conferencias}.

    Listings are newest-first; stops as soon as an entry predates `cutoff`
    instead of paginating through the full multi-administration archive.
    """
    source_type = "discurso" if section == "discursos" else "conferencia"
    page = 0
    while max_pages is None or page < max_pages:
        start = page * 40
        url = f"{CASAROSADA_BASE}/informacion/{section}" + (f"?start={start}" if start else "")
        response = _get(session, url, rate_limiter)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("div.item")
        if not items:
            break

        stop = False
        for item in items:
            link = item.select_one("a")
            time_el = item.select_one("time")
            title_el = item.select_one(".category-item-title")
            if link is None or time_el is None or title_el is None:
                continue
            entry_date = _parse_casarosada_date(time_el.get_text(strip=True))
            if entry_date is None:
                continue
            if entry_date < cutoff:
                stop = True
                break

            href = link.get("href", "")
            entry_id = _short_entry_id(href.rstrip("/").split("/")[-1])
            yield ListingEntry(
                source_type=source_type,
                entry_id=entry_id,
                title=title_el.get_text(strip=True),
                entry_date=entry_date,
                url=CASAROSADA_BASE + href if href.startswith("/") else href,
            )

        if stop:
            break
        page += 1


def fetch_casarosada_text(url: str, session: requests.Session, rate_limiter: RateLimiter) -> str:
    response = _get(session, url, rate_limiter)
    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.select_one("article") or soup.select_one("div.item-page")
    if article is None:
        return ""
    paragraphs = [p.get_text(" ", strip=True) for p in article.find_all("p")]
    paragraphs = [p for p in paragraphs if p]
    title = soup.title.get_text(strip=True) if soup.title else ""
    if paragraphs and paragraphs[0].strip().lower() == title.strip().lower():
        paragraphs = paragraphs[1:]
    return "\n\n".join(paragraphs)


def iter_ministerio_economia_noticias(
    cutoff: date,
    session: requests.Session,
    rate_limiter: RateLimiter,
    max_pages: Optional[int] = None,
) -> Iterator[ListingEntry]:
    """Yield entries from argentina.gob.ar/economia/noticias (Drupal, 0-indexed `?page=N`)."""
    page = 0
    while max_pages is None or page < max_pages:
        url = ECONOMIA_NOTICIAS_URL + (f"?page={page}" if page else "")
        response = _get(session, url, rate_limiter)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("a.panel.panel-default")
        if not items:
            break

        stop = False
        for item in items:
            time_el = item.select_one("time[datetime]")
            title_el = item.select_one("h3")
            href = item.get("href", "")
            if time_el is None or title_el is None or not href:
                continue
            raw_dt = time_el.get("datetime", "")
            try:
                entry_date = datetime.strptime(raw_dt[:10], "%Y-%m-%d").date()
            except ValueError:
                continue
            if entry_date < cutoff:
                stop = True
                break

            entry_id = _short_entry_id(href.rstrip("/").split("/")[-1])
            full_url = href if href.startswith("http") else f"https://www.argentina.gob.ar{href}"
            yield ListingEntry(
                source_type="comunicado_economia",
                entry_id=entry_id,
                title=title_el.get_text(strip=True),
                entry_date=entry_date,
                url=full_url,
            )

        if stop:
            break
        page += 1


def fetch_noticia_text(url: str, session: requests.Session, rate_limiter: RateLimiter) -> str:
    response = _get(session, url, rate_limiter)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.select_one("div.panel-pane.pane-texto") or soup.select_one("article")
    if body is None:
        return ""
    return body.get_text("\n\n", strip=True)


def _load_existing_ids(index_path: Path) -> set:
    existing = set()
    if index_path.exists():
        with open(index_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing.add((row["source_type"], row["entry_id"]))
    return existing


def scrape_all(
    out_dir: Path,
    cutoff: date = MILEI_INAUGURATION,
    max_pages_per_source: Optional[int] = None,
) -> Path:
    """Scrape all three sources into `out_dir`, writing one .txt per item plus an index.csv.

    Idempotent: an item already present in index.csv is not re-downloaded,
    so a full historical run can be safely interrupted and resumed.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    rate_limiter = RateLimiter(
        delays={
            "www.casarosada.gob.ar": 1.5,
            "www.argentina.gob.ar": 10.0,  # per argentina.gob.ar/robots.txt Crawl-delay
        },
        default_delay=2.0,
    )
    session = requests.Session()
    index_path = out_dir / "index.csv"
    existing_ids = _load_existing_ids(index_path)
    write_header = not index_path.exists()

    def process(entries: Iterator[ListingEntry], fetch_fn) -> Iterator[Tuple[str, ...]]:
        for entry in entries:
            if (entry.source_type, entry.entry_id) in existing_ids:
                continue
            text = fetch_fn(entry.url, session, rate_limiter)
            if not text:
                continue
            filename = f"{entry.source_type}_{entry.entry_id}.txt"
            (out_dir / filename).write_text(text, encoding="utf-8")
            existing_ids.add((entry.source_type, entry.entry_id))
            yield (
                entry.source_type,
                entry.entry_id,
                entry.entry_date.isoformat(),
                entry.title,
                entry.url,
                filename,
            )

    with open(index_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["source_type", "entry_id", "date", "title", "url", "filename"])

        for row in process(
            iter_casarosada_section("discursos", cutoff, session, rate_limiter, max_pages_per_source),
            fetch_casarosada_text,
        ):
            writer.writerow(row)
            f.flush()

        for row in process(
            iter_casarosada_section("conferencias", cutoff, session, rate_limiter, max_pages_per_source),
            fetch_casarosada_text,
        ):
            writer.writerow(row)
            f.flush()

        for row in process(
            iter_ministerio_economia_noticias(cutoff, session, rate_limiter, max_pages_per_source),
            fetch_noticia_text,
        ):
            writer.writerow(row)
            f.flush()

    return index_path
