"""
main.py

Entry point for running the assessment extractor workflow.
"""

import logging
from pathlib import Path
from parser import parse_document
from analysis import summarize_dataframe
from exporter import export_to_word, export_to_excel

logging.basicConfig(level=logging.INFO)

def main():
    # Always resolve input path relative to this script's parent directory
    script_dir = Path(__file__).resolve().parent.parent
    input_dir = script_dir / "input"
    input_dir.mkdir(exist_ok=True)

    docx_files = list(input_dir.glob("*.docx"))
    if not docx_files:
        print(f"No DOCX files found in {input_dir}")
        return

    doc_path = str(docx_files[0])
    print(f"Using: {doc_path}")

    df = parse_document(doc_path)
    summarize_dataframe(df)

    # Example export (uncomment as needed)
    # export_to_word(df, script_dir / "output" / "output.docx")
    # export_to_excel(df, script_dir / "output" / "output.xlsx")

if __name__ == "__main__":
    main()