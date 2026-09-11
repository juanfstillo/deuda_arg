# CLAUDE.md — Project North Star

## What this repo is

A political-economy research project (Juan Stillo & Julián) for a UBA cátedra presentation, aimed to scale into a congress paper. One core puzzle, two data tracks that feed the same argument:

**Core puzzle:** How does macroeconomic sovereign debt rollover force microeconomic household debt crises in Argentina, and how does the executive use blame-avoidance rhetoric to survive the political fallout? Put another way — **does the regulatory/fiscal design protect the financial system (bondholders, banks) or the people bearing the adjustment (borrowers, taxpayers)?**

The repo has two subprojects. They are not competing drafts — they answer different halves of the same question and are meant to be cross-referenced in the final paper.

- **`general_proyect/`** — Track 2: the household-credit side. Mora crediticia, BCRA regulatory design (rate caps, LEFIs, bank/fintech asymmetry), deuda/ingreso. Has its own `README.md`, `pyproject.toml` (Python 3.11, Poetry), and `CLAUDE.md`-equivalent context in `docs/planteo_catedra.md`.
- **`vreeland/`** — Track 1: the sovereign/rhetoric side. NLP engine over presidential/Ministry of Economy speeches, quantifying blame-avoidance and IMF-conditionality language. Own `requirements.txt` (plain pip, no Poetry).

**Before building anything new, check both subprojects for existing work.** Both have already had substantial architecture built in separate sessions (one with Gemini, one here) — duplicated effort has already happened once (see Track 1 status below); don't repeat it.

## Theoretical frameworks (operationalized, not decorative)

Full 48-hour translation memos live in `general_proyect/docs/*_48_h_*.md` and `vreeland/48-H.md`. Read those before writing analysis code that touches theory — they already map each framework to specific Argentine empirical referents and testable hypotheses. Summary:

- **Stigler (1971) — regulatory capture:** concentrated industries (banks, bondholders) organize cheaply and capture the regulator; diffuse publics (taxpayers, borrowers) can't organize, so regulation serves the regulated. Argentine analogue: reserve-requirement/liquidity rules (LEFIs, LECAPs) that force or reward banks for holding sovereign debt.
- **Peltzman (1976) — political support maximization:** politicians don't grant industries pure rents (that's electorally suicidal); they cross-subsidize, spreading pain across concentrated and diffuse groups to maximize *total* political support, not to serve one side purely. Argentine analogue: how fiscal-adjustment pain is split between bondholders and voters facing austerity.
- **Weaver (1986) — blame avoidance:** voters punish losses harder than they reward gains, so politicians facing mandatory pain switch from credit-claiming to blame-minimization via three concrete strategies — **use these three as the actual coding categories, not one flat "blame_avoidance" bucket**:
  1. **Passing the Buck** — delegating to an external authority (keywords: `FMI`, `metas`, `acuerdo`, `condicionalidad`).
  2. **Scapegoating** — blaming a prior administration or external shock (keywords: `herencia`, `pesada herencia`, `fiesta`, `gobierno anterior`).
  3. **Redefining the Issue / TINA** — framing the policy as inevitable, not chosen (keywords: `abismo`, `inevitable`, `no hay alternativa`, `ajuste estructural`).
- **Vreeland (2003) — strategic IMF conditionality:** executives *choose* to sign IMF agreements even without acute need, to use external conditionality as leverage against domestic veto players (congress, unions) — "the IMF made me do it" is a feature, not a bug, for the signing government. Testable hypothesis already identified in the memo: blame-avoidance/IMF rhetoric should spike when the executive has *fewer* legislative seats (more veto players to overcome), not simply when debt is highest.
- **Policy feedback:** past regulatory design changes the incentive landscape for future rounds (e.g., the 2024 LEFI creation → 2025 LEFI wind-down → bank funding-cost shift → possible pass-through to lending rates → mora). See `general_proyect/docs/planteo_catedra.md` §2.4 for a worked, honestly-inconclusive test of this against real BCRA rate series.

## Track 2 status (`general_proyect/`) — further along

- `src/bcra_api.py`: working, live-tested client for BCRA's Principales Variables (v4.0) and Central de Deudores (v1.0) APIs. Central de Deudores is per-CUIT lookup only — **no aggregate mora-by-entity exists via API**; that requires manually downloading BCRA's "Anexo estadístico del Informe sobre Bancos" Excel.
- `docs/planteo_catedra.md`: the full argument outline mapping each theory to a specific regulatory event (rate cap removal May 2024, LEFI asymmetry/wind-down), plus a rival macro hypothesis to rule out (inflation/real-wage erosion) before crediting any effect to regulatory design.
- Open: aggregate mora Excel download + parser, EPH income cross-reference, a cleaner (daily/event-study) test of the LEFI rate-break hypothesis.

## Track 1 status (`vreeland/`) — scaffold built and runs, lexicon is not yet theory-accurate

A full pipeline already exists and executes end-to-end on sample data: `speech_analyzer/{scraper,preprocessor,analyzer,storage}.py`, `main.py` (CLI), `tests/test_analysis.py` (passing), output verified in `data/output/speech_metrics.csv`.

**Resolved since the initial handoff:**
1. `analyzer.py`'s keyword taxonomy was rebuilt into 5 theory-grounded categories: Weaver's `passing_the_buck` / `scapegoating` / `redefining_issue_tina`, Vreeland's `fmi_conditionality` (kept distinct — expected to co-occur with `passing_the_buck` on IMF text, that's a real feature not a bug), and `responsabilizacion_individual` (Hood-style, seeded from the Aug-2026 episodes in `marco_teorico.md`). Accent-insensitive matching added via `preprocessor.fold_accents` without touching `normalize_text`'s accent-preserving contract (another test relies on that).
2. A real crawler now exists: `speech_analyzer/gov_scraper.py` + `scrape_speeches.py`, covering all three confirmed sources — casarosada.gob.ar `/informacion/discursos` and `/informacion/conferencias` (Joomla, `div.item` listings), and argentina.gob.ar `/economia/noticias` (Drupal, `?page=N`). Selectors were derived from real fetched HTML, not guessed. Rate limits are real, not placeholders: 1.5s self-imposed on casarosada.gob.ar (its robots.txt sets none), exactly 10s on argentina.gob.ar (its robots.txt mandates `Crawl-delay: 10`). Scoped to Dec 2023–present (Milei term) per the confirmed decision — 219 discursos + 237 conferencias + 455 comunicados = 911 items total. Idempotent: `index.csv` tracks what's already downloaded, so a run can be interrupted/resumed safely. A full backfill costs ~90 minutes, almost entirely the mandated Ministry delay (455 × 10s).

**Still open:**
1. No link yet between speech-metrics output and the veto-player variable (legislative seat share) that the Vreeland memo's testable hypothesis actually needs.
2. Environment mismatch: `vreeland/` uses plain pip + `requirements.txt` against Python 3.9 locally; `general_proyect/` uses Poetry + Python 3.11. Not urgent to unify, but don't assume one env when working in the other.
3. Whether the scraped raw corpus (`vreeland/data/raw/gov_sources/`, ~911 text files) should be committed to git or kept local-only/regenerated — not yet decided.

## Conventions

- Docs for Track 2 (`general_proyect/`) are in Spanish, matching the cátedra audience. Docs and code comments for Track 1 (`vreeland/`) are in English (that's how they were authored) — don't force a translation pass, just don't mix languages within one file.
- Don't invent regulatory dates, communication numbers, or figures — verify against primary sources (BCRA comunicaciones, OPC reports) the way `planteo_catedra.md` already does, and mark anything unverified as pending rather than asserting it.
