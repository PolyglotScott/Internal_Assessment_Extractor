"""
analysis.py

Provides functions for sorting, summarizing, and reporting on parsed assessment data.
"""

import logging

logger = logging.getLogger(__name__)

def summarize_dataframe(df):
    """
    Logs a summary breakdown of chapters, processes, questions, and answers.
    """
    chapters = df['Chapter'].dropna().unique()
    processes = df[['Chapter', 'Process']].drop_duplicates().dropna(subset=['Process'])
    questions = df[df['Questions'] != '']
    answers = df[df['Answer'] != '']

    logger.info("Summary breakdown:")
    logger.info("Total chapters: %d", len(chapters))
    logger.info("Total processes: %d", len(processes))
    logger.info("Total questions: %d", len(questions))
    logger.info("Total answers: %d", len(answers))

    for chapter in chapters:
        chapter_df = df[df['Chapter'] == chapter]
        chapter_processes = chapter_df['Process'].dropna().unique()
        logger.info("Chapter: '%s' | Processes: %d", chapter, len(chapter_processes))
        for process in chapter_processes:
            process_df = chapter_df[chapter_df['Process'] == process]
            q_count = process_df[process_df['Questions'] != ''].shape[0]
            a_count = process_df[process_df['Answer'] != ''].shape[0]
            logger.info("  Process: '%s' | Questions: %d | Answers: %d", process, q_count, a_count)