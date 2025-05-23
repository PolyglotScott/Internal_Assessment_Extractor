"""
analysis.py

Provides functions for sorting, summarizing, and reporting on parsed assessment data.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)

def summarize_dataframe(df: pd.DataFrame):
    """
    Print a summary of the DataFrame, including shape and column info.
    """
    print("Summary:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("Column names:", ", ".join(df.columns))
    print("First 5 rows:")
    print(df.head())

def analyze_complex():
    """
    Example function that demonstrates handling many local variables.
    """
    # Split variables into logical groups to avoid too many locals
    group1 = list(range(7))   # a, b, c, d, e, f, g
    group2 = list(range(7, 14))  # h, i, j, k, l, m, n
    group3 = list(range(14, 19))  # o, p, q, r, s

    result = sum(group1) + sum(group2) + sum(group3)
    print(
        "This is a demonstration of a function with many local variables. "
        f"The result is: {result}"
    )
    print(
        "Details: This is a very long line that should be split into multiple lines for "
        "readability and to comply with the 100 character limit."
    )

def old_summarize_dataframe(df: pd.DataFrame):
    """
    Logs a summary breakdown of chapters, processes, subsections, question types, questions, and answers.
    """
    chapters = df['Chapter'].dropna().unique()
    processes = (
        df[['Chapter', 'Process']]
        .drop_duplicates()
        .dropna(subset=['Process'])
    )
    subsections = (
        df[['Chapter', 'Process', 'Subsection']]
        .drop_duplicates()
        .dropna(subset=['Subsection'])
    )
    question_types = df['QuestionType'].dropna().unique()
    questions = df[df['Questions'] != '']
    answers = df[df['Answer'] != '']

    logger.info("Summary breakdown:")
    logger.info("Total chapters: %d", len(chapters))
    logger.info("Total processes: %d", len(processes))
    logger.info("Total subsections: %d", len(subsections))
    logger.info("Total question types: %d", len(question_types))
    logger.info("Total questions: %d", len(questions))
    logger.info("Total answers: %d", len(answers))

    for chapter in chapters:
        chapter_df = df[df['Chapter'] == chapter]
        chapter_processes = chapter_df['Process'].dropna().unique()
        logger.info(
            "Chapter: '%s' | Processes: %d",
            chapter,
            len(chapter_processes)
        )
        for process in chapter_processes:
            process_df = chapter_df[chapter_df['Process'] == process]
            process_subsections = process_df['Subsection'].dropna().unique()
            logger.info(
                "  Process: '%s' | Subsections: %d",
                process,
                len(process_subsections)
            )
            for subsection in process_subsections:
                subsection_df = process_df[process_df['Subsection'] == subsection]
                q_count = subsection_df[subsection_df['Questions'] != ''].shape[0]
                a_count = subsection_df[subsection_df['Answer'] != ''].shape[0]
                logger.info(
                    "    Subsection: '%s' | Questions: %d | Answers: %d",
                    subsection,
                    q_count,
                    a_count
                )
            # Reduce local variables by using a tuple
            process_counts = (
                process_df[process_df['Questions'] != ''].shape[0],
                process_df[process_df['Answer'] != ''].shape[0]
            )
            logger.info(
                "  Process Total: Questions: %d | Answers: %d",
                process_counts[0],
                process_counts[1]
            )
        for qtype in question_types:
            qtype_count = chapter_df[chapter_df['QuestionType'] == qtype].shape[0]
            logger.info(
                "  QuestionType: '%s' | Count: %d",
                qtype,
                qtype_count
            )
