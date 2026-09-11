from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable, List, Dict, Any

import pandas as pd


def export_results(results: Iterable[Dict[str, Any]], output_csv: str | Path, db_path: str | Path | None = None) -> pd.DataFrame:
    rows = list(results)
    dataframe = pd.DataFrame(rows)

    csv_path = Path(output_csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(csv_path, index=False)

    if db_path is not None:
        db_file = Path(db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(db_file) as connection:
            dataframe.to_sql("speech_metrics", connection, if_exists="replace", index=False)

    return dataframe


def analyze_documents(documents: Iterable[Dict[str, Any]], analyzer) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for document in documents:
        text = document.get("text", "")
        metrics = analyzer.analyze_text(text)
        for metric in metrics:
            rows.append(
                {
                    "source": document.get("source", "unknown"),
                    "category": metric["category"],
                    "keywords": "; ".join(metric["keywords"]),
                    "count": metric["count"],
                    "density": metric["density"],
                }
            )
    return rows
