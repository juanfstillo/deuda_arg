from __future__ import annotations

import re
from typing import Dict, Iterable, List, Sequence

from .preprocessor import normalize_text, tokenize_text


class SpeechAnalyzer:
    """Detect and quantify political-economy text patterns."""

    DEFAULT_KEYWORDS = {
        "blame_avoidance": [
            "crisis",
            "anterior gobierno",
            "gobierno anterior",
            "responsabilidad",
            "deuda",
            "externa",
            "institucion externa",
            "institución externa",
            "fuerza mayor",
            "choque externo",
            "mandato",
            "estructura",
            "necesidad estructural",
            "ajuste estructural",
            "delegar",
            "delegación",
            "responsabilidad",
            "transferir",
            "restringir",
        ],
        "strategic_conditionality": [
            "fmi",
            "imf",
            "acuerdo con el fmi",
            "programa con el fmi",
            "condiciones",
            "ajuste",
            "recorte",
            "recortar",
            "gastos",
            "subsidios",
            "fiscal",
            "deuda",
            "prestamo",
            "préstamo",
            "externo",
            "compromiso",
            "reforma",
            "moneda",
        ],
    }

    def __init__(self, keyword_map: Dict[str, Sequence[str]] | None = None):
        self.keyword_map = dict(self.DEFAULT_KEYWORDS)
        if keyword_map:
            self.keyword_map.update(keyword_map)

    def _count_keyword_matches(self, text: str, keyword: str) -> int:
        normalized = normalize_text(text)
        pattern = r"\b" + re.escape(keyword) + r"\b"
        return len(re.findall(pattern, normalized))

    def analyze_text(self, text: str) -> List[Dict[str, object]]:
        if text is None:
            text = ""

        normalized = normalize_text(text)
        tokens = tokenize_text(normalized)
        total_tokens = len(tokens)
        results: List[Dict[str, object]] = []

        for category, keywords in self.keyword_map.items():
            count = 0
            for keyword in keywords:
                count += self._count_keyword_matches(normalized, keyword)
            density = (count / total_tokens * 100.0) if total_tokens else 0.0
            results.append(
                {
                    "category": category,
                    "keywords": list(keywords),
                    "count": count,
                    "density": density,
                }
            )

        return results

    def summarize(self, text: str) -> Dict[str, float]:
        metrics = self.analyze_text(text)
        return {
            metric["category"]: float(metric["density"]) for metric in metrics
        }
