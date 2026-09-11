# Task: Build a Political Economy Speech Analysis Engine in Python

## Context & Theoretical Background
This script is part of an academic project analyzing sovereign debt management, structural austerity, and blame-avoidance politics in Argentina. 
We operationalize two theoretical mechanisms:
1. **R. Kent Weaver (1986) — Blame Avoidance:** Politicians prioritize dodging blame over claiming credit, relying on strategies such as *Passing the Buck* (delegation to external institutions), *Scapegoating* (blaming previous administrations or external shocks), and *Redefining the Issue* (framing painful measures as structural necessities / TINA).
2. **James Raymond Vreeland (2003) — Strategic Conditionality:** Sovereign executives intentionally enter multilateral agreements (e.g., the IMF) to use loan conditions as political leverage to enforce unpopular domestic spending and subsidy cuts.

## Objective
Create a modular Python command-line application that ingests, cleans, and analyzes transcripts of official speeches/press releases (e.g., Argentine Executive / Ministry of Economy), detects and quantifies theoretical keyword categories, and exports the metrics to a structured CSV and SQLite database.

---

## Technical Specifications

### 1. Project Structure
Organize the code cleanly:
```text
speech_analyzer/
│
├── data/
│   ├── raw/                 # Downloaded raw text/html files
│   └── output/              # Processed CSVs and SQLite database
│
├── src/
│   ├── __init__.py
│   ├── scraper.py           # Scrapes official speeches (or parses local directory)
│   ├── preprocessor.py      # Text cleaning, normalization, tokenization (Spanish)
│   ├── analyzer.py          # Lexicon matching and density computation
│   └── storage.py           # Exports results to Pandas DataFrame, CSV, and SQLite
│
├── main.py                  # CLI entrypoint (using argparse or click)
└── requirements.txt         # Dependencies (requests, beautifulsoup4, pandas, etc.)