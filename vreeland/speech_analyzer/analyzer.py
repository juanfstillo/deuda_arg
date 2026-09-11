from __future__ import annotations

import re
from typing import Dict, List, Sequence

from .preprocessor import fold_accents, normalize_text, tokenize_text


class SpeechAnalyzer:
    """Detect and quantify blame-avoidance / conditionality rhetoric in Spanish political speech.

    Categories are not generic sentiment buckets — each maps to a specific
    mechanism from the project's theoretical memos (see `general_proyect/docs/`
    and `vreeland/48-H.md`), and the keyword lists are seeded from real,
    dated episodes documented in `general_proyect/docs/marco_teorico.md`
    §2.2 (Milei 03/08/2026, Gobierno 15/08/2026, BCRA 27-28/08/2026), not
    invented in the abstract:

    - `passing_the_buck` (Weaver 1986): delegating agency to an external,
      non-IMF-specific authority (markets, rating agencies, prior
      commitments) so the speaker isn't the one deciding.
    - `scapegoating` (Weaver 1986): blaming a prior administration or an
      external shock for the current pain.
    - `redefining_issue_tina` (Weaver 1986): framing the policy as
      inevitable/structural rather than a choice ("there is no alternative").
    - `fmi_conditionality` (Vreeland 2003): IMF-specific leverage language —
      kept separate from `passing_the_buck` because Vreeland's claim is
      narrower (the executive *chooses* external conditionality as leverage
      against domestic veto players, not just blame diffusion). The two
      categories are expected to co-occur on the same IMF-related text —
      that overlap is a real feature of the argument, not a bug to engineer
      away with mutually exclusive keyword sets.
    - `responsabilizacion_individual` (Hood 2011's presentational/policy
      strategies, per marco_teorico.md §2.2): reframing mora as a private
      matter between individuals and lenders rather than a policy design
      question. This doesn't fit Weaver's original three-strategy typology
      cleanly, but it's the pattern actually documented in the Aug-2026
      episodes, so it gets its own category instead of being forced into one
      of the other three.
    """

    DEFAULT_KEYWORDS = {
        "passing_the_buck": [
            "los mercados",
            "las calificadoras",
            "riesgo pais",
            "no fue una decision nuestra",
            "no fue nuestra decision",
            "no depende de nosotros",
            "nos obliga",
            "nos obligan",
            "no tenemos margen",
            "compromisos externos",
            "institucion externa",
            "organismos internacionales",
            "acreedores",
        ],
        "scapegoating": [
            "herencia",
            "pesada herencia",
            "la fiesta",
            "gobierno anterior",
            "kirchnerismo",
            "populismo",
            "anos de populismo",
            "nos dejaron",
            "el desastre que recibimos",
            "legado",
        ],
        "redefining_issue_tina": [
            "abismo",
            "inevitable",
            "no hay alternativa",
            "no hay plata",
            "ajuste estructural",
            "necesidad estructural",
            "unica salida",
            "camino inexorable",
            "ley de hierro",
        ],
        "fmi_conditionality": [
            "fmi",
            "imf",
            "acuerdo con el fmi",
            "programa con el fmi",
            "board del fmi",
            "staff report",
            "metas fiscales",
            "condicionalidad",
            "acuerdo de facilidades extendidas",
            "programa con el fondo",
            "desembolso",
            "revision del fondo",
        ],
        "responsabilizacion_individual": [
            "problema entre privados",
            "cuestion entre privados",
            "riesgo moral",
            "decision individual",
            "nadie los obligo",
            "les puso una pistola en la cabeza",
            "decisiones informadas",
            "educacion financiera",
            "letra chica",
        ],
    }

    def __init__(self, keyword_map: Dict[str, Sequence[str]] | None = None):
        self.keyword_map = dict(self.DEFAULT_KEYWORDS)
        if keyword_map:
            self.keyword_map.update(keyword_map)

    def _count_keyword_matches(self, folded_text: str, keyword: str) -> int:
        folded_keyword = fold_accents(keyword.lower())
        pattern = r"\b" + re.escape(folded_keyword) + r"\b"
        return len(re.findall(pattern, folded_text))

    def analyze_text(self, text: str) -> List[Dict[str, object]]:
        if text is None:
            text = ""

        normalized = normalize_text(text)
        folded = fold_accents(normalized)
        tokens = tokenize_text(normalized)
        total_tokens = len(tokens)
        results: List[Dict[str, object]] = []

        for category, keywords in self.keyword_map.items():
            count = 0
            for keyword in keywords:
                count += self._count_keyword_matches(folded, keyword)
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
