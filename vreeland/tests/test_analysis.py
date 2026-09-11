from speech_analyzer.analyzer import SpeechAnalyzer
from speech_analyzer.preprocessor import fold_accents, normalize_text, tokenize_text


def test_normalize_and_tokenize_text():
    text = "  ¡La economía y la política!  "
    normalized = normalize_text(text)
    tokens = tokenize_text(normalized)

    assert "economía" in normalized
    assert "economía" in tokens
    assert "política" in tokens


def test_fold_accents_strips_diacritics_without_touching_normalize_text():
    assert fold_accents("decisión") == "decision"
    assert fold_accents("año") == "ano"
    # normalize_text itself must keep accents (other code relies on that)
    assert normalize_text("decisión") == "decisión"


def test_analyzer_detects_all_five_categories():
    analyzer = SpeechAnalyzer()
    text = (
        "La crisis heredada del gobierno anterior nos obliga a tomar medidas dificiles. "
        "No fue una decision nuestra: el acuerdo con el FMI establece condiciones claras. "
        "Este ajuste estructural no es una eleccion politica, sino una necesidad estructural. "
        "Al final, la mora es un problema entre privados y una decision individual de cada familia."
    )

    result = analyzer.analyze_text(text)
    categories = {item["category"]: item for item in result}

    expected_categories = {
        "passing_the_buck",
        "scapegoating",
        "redefining_issue_tina",
        "fmi_conditionality",
        "responsabilizacion_individual",
    }
    assert expected_categories == set(categories)

    # Each category should fire at least once on this text, since it was
    # built to hit all five (mirrors the real documented episodes).
    for category, metric in categories.items():
        assert metric["count"] >= 1, f"{category} did not match any keyword"
        assert metric["density"] > 0


def test_analyzer_is_accent_insensitive():
    analyzer = SpeechAnalyzer()
    with_accents = analyzer.analyze_text("La decisión individual y el riesgo moral son claves.")
    without_accents = analyzer.analyze_text("La decision individual y el riesgo moral son claves.")

    density_with = {m["category"]: m["density"] for m in with_accents}
    density_without = {m["category"]: m["density"] for m in without_accents}

    assert density_with["responsabilizacion_individual"] == density_without["responsabilizacion_individual"]
    assert density_with["responsabilizacion_individual"] > 0
