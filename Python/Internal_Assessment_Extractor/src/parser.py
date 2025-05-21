"""
parser.py

Module for parsing DOCX documents to extract chapters, processes,
and question-answer pairs for internal assessment extraction.

Includes functions to extract questions/answers from table cells and
parse the entire document into a structured DataFrame.
"""

import logging
from docx import Document
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_question_answer(cell_text: str):
    """
    Extract question and answer from cell text if it contains 'ASK participants:' and 'ANSWER:'.

    Args:
        cell_text (str): The text content of a table cell.

    Returns:
        tuple: (question, answer) or (None, None) if not properly found.
    """
    question = None
    answer = None
    try:
        if 'ASK participants:' in cell_text and 'ANSWER:' in cell_text:
            question_part = cell_text.split('ASK participants:')[1]
            question = question_part.split('ANSWER:')[0].strip()
            answer = question_part.split('ANSWER:')[1].strip()
            logger.debug("Extracted Q: %s | A: %s", question, answer)
    except (IndexError, AttributeError) as exc:
        logger.warning("Failed to extract Q&A from cell text due to %s: %s", exc, cell_text)
    return question, answer

def extract_chapters_processes(doc):
    """
    Extract chapters and processes from document paragraphs.

    Args:
        doc (Document): The loaded DOCX document object.

    Returns:
        tuple: current_chapter (str), current_process (str), list of initial rows with chapter/process context.
    """
    current_chapter = ""
    current_process = ""
    table_data = []

    for para in doc.paragraphs:
        style = para.style.name if para.style else ""
        text = para.text.strip()

        if style in ['Heading 1', 'Header 2']:
            current_chapter = text
            logger.info("Found chapter: %s", current_chapter)
            table_data.append([current_chapter, '', '', current_chapter, current_process])
        elif style in ['Heading 2', 'Header 3']:
            current_process = text
            logger.info("Found process: %s", current_process)
            table_data.append(['', '', '', current_chapter, current_process])
    return current_chapter, current_process, table_data

def extract_qa_from_tables(doc, current_chapter, current_process):
    """
    Extract question-answer pairs from tables in the document.

    Args:
        doc (Document): The loaded DOCX document object.
        current_chapter (str): The current chapter name to associate Q&A with.
        current_process (str): The current process name to associate Q&A with.

    Returns:
        list: List of extracted Q&A rows with metadata.
    """
    table_data = []
    for table_idx, table in enumerate(doc.tables):
        for row_idx, row in enumerate(table.rows):
            for cell_idx, cell in enumerate(row.cells):
                cell_text = cell.text.strip()
                if ('CONCEPT CHECK' in cell_text and 
                    'ASK participants:' in cell_text and 
                    'ANSWER:' in cell_text):
                    question, answer = extract_question_answer(cell_text)
                    if question and answer:
                        table_data.append([question, answer, '/1', current_chapter, current_process])
                        logger.debug("Added Q&A from table[%d] row[%d] cell[%d]", table_idx, row_idx, cell_idx)
    return table_data

def parse_document(doc_path: str):
    """
    Parses the DOCX document, extracting chapters, processes, and Q&A.

    Args:
        doc_path (str): Path to the DOCX file.

    Returns:
        pd.DataFrame: DataFrame containing Questions, Answers, Marks, Chapter, and Process.
    """
    try:
        doc = Document(doc_path)
    except Exception as exc:
        logger.error("Failed to load document: %s | Error: %s", doc_path, exc)
        raise

    current_chapter, current_process, table_data = extract_chapters_processes(doc)
    qa_data = extract_qa_from_tables(doc, current_chapter, current_process)
    table_data.extend(qa_data)

    df = pd.DataFrame(table_data, columns=['Questions', 'Answer', 'Marks', 'Chapter', 'Process'])
    df_cleaned = df[(df['Questions'] != '') | (df['Answer'] != '')].reset_index(drop=True)
    logger.info("Finished parsing document. Total Q&A extracted: %d", len(df_cleaned))

    return df_cleaned

if __name__ == "__main__":
    DOC_PATH = "C:/Users/vivif/Documents/Code/Python/Internal_Assessment_Extractor/input/Module 3 - NTS Financial Services Systems Overview - Facilitator Guide - V1.docx"

    df_questions = parse_document(DOC_PATH)
    print(df_questions.head(15))
