from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from speech_analyzer.gov_scraper import MILEI_INAUGURATION, scrape_all


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scrape presidential speeches (casarosada.gob.ar/informacion/discursos), "
            "press conferences (.../conferencias), and Ministerio de Economía press "
            "releases (argentina.gob.ar/economia/noticias) into local .txt files."
        )
    )
    parser.add_argument(
        "--out-dir",
        default="data/raw/gov_sources",
        help="Directory to write .txt files + index.csv (default: data/raw/gov_sources)",
    )
    parser.add_argument(
        "--since",
        default=MILEI_INAUGURATION.isoformat(),
        help="ISO date cutoff (YYYY-MM-DD). Stops paginating a source once its entries "
        "predate this date. Default: 2023-12-10 (Milei inauguration).",
    )
    parser.add_argument(
        "--max-pages-per-source",
        type=int,
        default=None,
        help="Cap listing pages per source. Use a small number (e.g. 1) for a smoke "
        "test before running the full historical backfill.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cutoff = date.fromisoformat(args.since)
    index_path = scrape_all(Path(args.out_dir), cutoff=cutoff, max_pages_per_source=args.max_pages_per_source)
    print(f"Done. Index written to {index_path}")


if __name__ == "__main__":
    main()
