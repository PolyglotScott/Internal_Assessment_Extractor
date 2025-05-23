"""
utils.py

This module provides utility functions for text cleaning, paragraph style checking,
table data extraction from Word documents, and structured logging for document processing tasks.
"""

import logging
from typing import List, Dict
from docx.table import Table
from docx.text.paragraph import Paragraph

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    """
    Clean and normalise extracted text by trimming leading/trailing whitespace
    and collapsing multiple spaces into a single space.

    Args:
        text (str): The input text string.

    Returns:
        str: A cleaned and normalised version of the text.
    """
    if not text:
        return ''
    return ' '.join(text.strip().split())


def is_heading(paragraph: Paragraph, style_name: str) -> bool:
    """
    Determine if a Word paragraph matches a given heading style.

    Args:
        paragraph (Paragraph): The Word paragraph object.
        style_name (str): The expected style name (e.g., 'Heading 1').

    Returns:
        bool: True if the paragraph's style matches, else False.
    """
    try:
        return paragraph.style.name == style_name
    except AttributeError:
        logger.warning("Paragraph style check failed due to missing style: %s", paragraph.text)
        return False


def extract_table_data(table: Table) -> List[Dict[str, str]]:
    """
    Extract structured data from a Word table as a list of dictionaries.

    Assumes the first row is the header row, and each subsequent row
    represents a record.

    Args:
        table (Table): A python-docx Table object.

    Returns:
        List[Dict[str, str]]: A list where each item is a dictionary mapping
                              header names to cleaned cell text values.
    """
    try:
        headers = [clean_text(cell.text) for cell in table.rows[0].cells]
        rows = []

        for row_idx, row in enumerate(table.rows[1:], start=1):
            try:
                row_data = {
                    headers[i]: clean_text(cell.text)
                    for i, cell in enumerate(row.cells)
                    if i < len(headers)
                }
                rows.append(row_data)
            except IndexError as e:
                logger.warning("Failed to extract row %d due to mismatch: %s", row_idx, str(e))
                continue

        return rows

    except Exception as e:  # pylint: disable=broad-except
        logger.error("Table extraction failed: %s", str(e))
        return []


def log_info(message: str) -> None:
    """
    Log an informational message.

    Args:
        message (str): The message to log.
    """
    logger.info("%s", message)


def log_warning(message: str) -> None:
    """
    Log a warning message.

    Args:
        message (str): The message to log.
    """
    logger.warning("%s", message)


def log_error(message: str) -> None:
    """
    Log an error message.

    Args:
        message (str): The message to log.
    """
    logger.error("%s", message)


def setup_logging(level=logging.INFO):
    """
    Set up logging configuration.

    Args:
        level: Logging level (default: logging.INFO)
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def some_function():
    """
    Placeholder for some functionality.
    """
    # Implementation to be added
    # Remove unnecessary pass statement
    return


def another_function():
    """
    Placeholder for another functionality.
    """
    try:
        pass  # Placeholder for another functionality
    except (ValueError, TypeError) as exc:
        # Handle specific exceptions as appropriate
        print(f"Error: {exc}")
