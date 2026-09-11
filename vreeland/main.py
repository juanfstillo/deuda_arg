from __future__ import annotations

import argparse
from pathlib import Path

from speech_analyzer.analyzer import SpeechAnalyzer
from speech_analyzer.scraper import load_documents_from_directory, read_local_file
from speech_analyzer.storage import analyze_documents, export_results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Political economy speech analysis engine")
    parser.add_argument("--input", type=str, help="Path to a text/html file or folder of speech files")
    parser.add_argument("--output-csv", type=str, default="data/output/speech_metrics.csv", help="Output CSV path")
    parser.add_argument("--db-path", type=str, default="data/output/speech_metrics.db", help="SQLite database path")
    parser.add_argument("--skip-db", action="store_true", help="Skip SQLite export and only write the CSV")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input) if args.input else None

    if input_path is None:
        raise ValueError("You must provide --input with a file or directory path.")

    if input_path.is_dir():
        documents = load_documents_from_directory(input_path)
    else:
        documents = [{"source": str(input_path), "text": read_local_file(input_path)}]

    analyzer = SpeechAnalyzer()
    rows = analyze_documents(documents, analyzer)
    db_path = None if args.skip_db else args.db_path
    export_results(rows, args.output_csv, db_path)

    print(f"Processed {len(documents)} documents and exported {len(rows)} metrics rows.")


if __name__ == "__main__":
    main()
