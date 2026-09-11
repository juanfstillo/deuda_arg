from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

import requests
from bs4 import BeautifulSoup


def fetch_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return " ".join(soup.get_text(" ", strip=True).split())


def read_local_file(path: str | Path) -> str:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    if file_path.suffix.lower() == ".html":
        soup = BeautifulSoup(text, "html.parser")
        return " ".join(soup.get_text(" ", strip=True).split())
    return text


def load_documents_from_directory(directory: str | Path) -> List[Dict[str, Any]]:
    base_dir = Path(directory)
    documents: List[Dict[str, Any]] = []

    if not base_dir.exists():
        return documents

    for file_path in sorted(base_dir.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in {".txt", ".csv", ".md", ".html", ".htm"}:
            documents.append(
                {
                    "source": str(file_path),
                    "text": read_local_file(file_path),
                }
            )

    return documents
