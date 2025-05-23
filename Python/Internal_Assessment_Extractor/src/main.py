"""
main.py

Entry point for running the assessment extractor workflow.
"""

import logging
import time
import sys
from pathlib import Path
from dataclasses import dataclass
from .doc_parser import parse_document
from .analysis import summarize_dataframe
from .exporter import export_to_word, export_to_excel
from .cleaner import clean_data

logging.basicConfig(level=logging.INFO)

@dataclass
class ProgressInfo:
    """Data structure for tracking progress of file processing."""
    file_idx: int
    total_files: int
    stage_idx: int
    total_stages: int
    stage: str
    elapsed: float
    bar_length: int = 40

def print_progress(progress: ProgressInfo):
    """
    Print a progress bar for the current processing stage.
    """
    percent = (
        (progress.file_idx - 1) + (progress.stage_idx / progress.total_stages)
    ) / progress.total_files
    arrow = '-' * max(int(round(percent * progress.bar_length) - 1), 0) + '>'
    spaces = ' ' * (progress.bar_length - len(arrow))
    sys.stdout.write(
        f'\r[{arrow}{spaces}] {int(percent * 100)}% - File {progress.file_idx}/'
        f'{progress.total_files} - {progress.stage} | Elapsed: {progress.elapsed:.1f}s'
    )
    sys.stdout.flush()

def main():
    """
    Main workflow for processing assessment documents.
    """
    script_dir = Path(__file__).resolve().parent.parent
    input_dir = script_dir / "input"
    input_dir.mkdir(exist_ok=True)

    docx_files = list(input_dir.glob("*.docx"))
    total_files = len(docx_files)
    if not docx_files:
        logging.error("No DOCX files found in %s", input_dir)
        return

    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)

    stages = ["Parsing", "Summarizing", "Cleaning", "Exporting"]
    total_stages = len(stages)
    start_time = time.time()

    for file_idx, doc_path in enumerate(docx_files, 1):
        logging.info("Processing: %s", doc_path)
        try:
            elapsed = time.time() - start_time

            # Parsing
            print_progress(
                ProgressInfo(file_idx, total_files, 0, total_stages, stages[0], elapsed)
            )
            df = parse_document(str(doc_path))

            # Summarizing
            print_progress(
                ProgressInfo(file_idx, total_files, 1, total_stages, stages[1], elapsed)
            )
            summarize_dataframe(df)

            # Cleaning
            print_progress(
                ProgressInfo(file_idx, total_files, 2, total_stages, stages[2], elapsed)
            )
            df = clean_data(df)

            # Exporting
            print_progress(
                ProgressInfo(file_idx, total_files, 3, total_stages, stages[3], elapsed)
            )
            export_to_word(df, output_dir / f"{doc_path.stem}_cleaned.docx")
            export_to_excel(df, output_dir / f"{doc_path.stem}_cleaned.xlsx")

            # Completed this file
            print_progress(
                ProgressInfo(file_idx, total_files, 4, total_stages, "Completed", elapsed)
            )

        except Exception as exc:  # pylint: disable=broad-except
            logging.error("Failed to process %s: %s", doc_path, exc)

    elapsed = time.time() - start_time
    print(f"\nAll files processed in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
