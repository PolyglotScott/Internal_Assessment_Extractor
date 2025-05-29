"""
assessment_summary.py

Provides functions for logging a detailed breakdown of parsed assessment data.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)

def log_chapter_summary(df: pd.DataFrame, chapters, question_types):
    """
    Log summary information for each chapter, including the number of processes,
    and delegate to process summary logging.
    """
    for chapter in chapters:
        chapter_df = df[df['Chapter'] == chapter]
        chapter_processes = chapter_df['Process'].dropna().unique()
        logger.info(
            "Chapter: '%s' | Processes: %d",
            chapter,
            len(chapter_processes)
        )
        log_process_summary(chapter_df, chapter_processes, question_types)

def log_process_summary(chapter_df: pd.DataFrame, chapter_processes, question_types):
    """
    Log summary information for each process within a chapter, including the number of subsections,
    and delegate to subsection and question type summary logging.
    """
    for process in chapter_processes:
        process_df = chapter_df[chapter_df['Process'] == process]
        process_subsections = process_df['Subsection'].dropna().unique()
        logger.info(
            "  Process: '%s' | Subsections: %d",
            process,
            len(process_subsections)
        )
        log_subsection_summary(process_df, process_subsections)
        process_counts = (
            process_df[process_df['Questions'] != ''].shape[0],
            process_df[process_df['Answer'] != ''].shape[0]
        )
        logger.info(
            "  Process Total: Questions: %d | Answers: %d",
            process_counts[0],
            process_counts[1]
        )
    log_question_type_summary(chapter_df, question_types)

def log_subsection_summary(process_df: pd.DataFrame, process_subsections):
    """
    Log summary information for each subsection within a process, 
    including the number of questions and answers.
    """
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

def log_question_type_summary(chapter_df: pd.DataFrame, question_types):
    """
    Log summary information for each question type within a chapter, 
    including the count of each type.
    """
    for qtype in question_types:
        qtype_count = chapter_df[chapter_df['QuestionType'] == qtype].shape[0]
        logger.info(
            "  QuestionType: '%s' | Count: %d",
            qtype,
            qtype_count
        )

def summarize_assessment_breakdown(df: pd.DataFrame):
    """
    Logs a summary breakdown of chapters, processes, subsections, 
    question types, questions, and answers.
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

    log_chapter_summary(df, chapters, question_types)

    logger.info("Total unique questions: %d", df['Questions'].nunique())
    logger.info("Total unique answers: %d", df['Answer'].nunique())
    logger.info("Summary complete.")
