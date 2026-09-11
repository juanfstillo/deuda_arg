import re
import unicodedata
from typing import List


def normalize_text(text: str) -> str:
    """Lowercase, normalize accents, and compact whitespace."""
    if not text:
        return ""

    normalized = unicodedata.normalize("NFKC", text)
    normalized = normalized.lower()
    normalized = normalized.replace("\xa0", " ")
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def tokenize_text(text: str) -> List[str]:
    """Tokenize Spanish text while preserving accented characters."""
    cleaned = normalize_text(text)
    return re.findall(r"[a-záéíóúüñ]+(?:'[a-záéíóúüñ]+)?", cleaned)
