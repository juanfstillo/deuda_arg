from speech_analyzer.analyzer import SpeechAnalyzer
from speech_analyzer.preprocessor import normalize_text, tokenize_text


def test_normalize_and_tokenize_text():
    text = "  ¡La economía y la política!  "
    normalized = normalize_text(text)
    tokens = tokenize_text(normalized)

    assert "economía" in normalized
    assert "economía" in tokens
    assert "política" in tokens


def test_analyzer_detects_keyword_categories():
    analyzer = SpeechAnalyzer()
    text = (
        "La crisis fue provocada por el anterior gobierno. "
        "Necesitamos ajustar por la necesidad estructural. "
        "El acuerdo con el FMI nos obliga a recortar gastos. "
        "La responsabilidad se delega a la institución externa."
    )

    result = analyzer.analyze_text(text)
    categories = {item["category"]: item for item in result}

    assert "blame_avoidance" in categories
    assert "strategic_conditionality" in categories
    assert categories["blame_avoidance"]["count"] >= 1
    assert categories["strategic_conditionality"]["count"] >= 1
    assert categories["blame_avoidance"]["density"] >= 0
    assert categories["strategic_conditionality"]["density"] >= 0
