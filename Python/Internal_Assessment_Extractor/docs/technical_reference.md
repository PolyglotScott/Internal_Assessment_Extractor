# Technical Reference

## Overview

This document provides detailed technical information about the core components, data structures, and functions used in the **internall_assessment_extractor** project. It is intended for developers who want to understand the internal workings or contribute to the codebase.

---

## Core Modules

### `src/parser.py`

- Responsible for parsing Microsoft Word `.docx` files.
- Extracts assessment questions, answers, and associated metadata based on predefined styles (e.g., "Heading 1", "CONCEPT CHECK").
- Outputs the extracted data as structured pandas DataFrames.

**Key Functions:**

- `parse_docx(file_path: str) -> pandas.DataFrame`  
  Parses the specified DOCX file and returns a DataFrame containing extracted questions, answers, and marks.

---

### `src/exporter.py`

- Handles exporting the parsed data to a Word document (`.docx`) format.
- Applies formatting to mimic the original assessment style and structure.
- Supports additional export formats as a potential future enhancement.

**Key Functions:**

- `export_to_word(dataframe: pandas.DataFrame, output_path: str) -> None`  
  Takes a DataFrame of extracted data and creates a formatted Word document saved at `output_path`.

---

### `src/utils.py`

- Contains utility functions to assist with text processing, formatting, and repetitive tasks.
- Helps maintain clean separation of concerns and modular code design.

**Example Utility Functions:**

- `extract_text_from_paragraph(paragraph)` — Extracts clean text from a Word paragraph.
- `apply_styling_to_paragraph(paragraph, style_name)` — Applies a predefined style to a paragraph object.

---

## Data Structures

### Extracted DataFrame

The central data structure used throughout the project is a pandas DataFrame with the following typical columns:

| Column Name | Description                                      |
|-------------|------------------------------------------------|
| `chapter`   | The chapter or section heading (e.g., "Chapter 1") |
| `question`  | The text of the assessment question             |
| `answer`    | The corresponding answer or marking guide       |
| `marks`     | The allocated marks for the question             |
| `notes`     | Additional notes or comments (optional)          |

This structure enables easy manipulation, filtering, and exporting of assessment content.

---

## Parsing Logic

- The parser reads DOCX paragraphs and tables, searching for styles that indicate key content (e.g., questions in "CONCEPT CHECK" tables).
- Headings (e.g., "Heading 1", "Heading 2") are used to identify chapters and sub-sections.
- Tables containing question-answer pairs are processed row-by-row, extracting text and formatting data into the DataFrame.
- Error handling ensures robustness against malformed documents or unexpected formatting.

---

## Dependencies

| Package          | Version  | Purpose                                      |
|------------------|----------|----------------------------------------------|
| `python-docx`    | 1.1.2    | Reading and writing Microsoft Word `.docx` files |
| `pandas`         | 2.2.3    | Data manipulation and storage in DataFrames   |
| `numpy`          | 2.2.6    | Underlying numerical operations for pandas    |
| `python-dateutil`| 2.9.0.post0 | Date and time utilities (if required)      |

> Note: All dependencies are listed in `requirements.txt` for easy environment setup.

---

## Environment Setup

- Requires Python 3.8 or later.
- Virtual environment recommended to isolate dependencies.
- Install dependencies via:

```bash
pip install -r requirements.txt

---

## Future Enhancements (Technical Perspective)

- Extend parser to support additional question styles and formats.
- Implement direct export to formats such as CSV, JSON, or Excel.
- Introduce command-line interface (CLI) flags for advanced usage.
- Add detailed logging and error reporting.
- Support for integration into CI/CD pipelines for automated document processing.

---

## Contact and Support

For technical questions or contributions, please contact:

**Scott Maxwell**  
GitHub: [PolyglotScott](https://github.com/PolyglotScott)  
Email: [scott.maxwell.polyglot@gmail.com](mailto:scott.maxwell.polyglot@gmail.com)

---

*End of Technical Reference*
