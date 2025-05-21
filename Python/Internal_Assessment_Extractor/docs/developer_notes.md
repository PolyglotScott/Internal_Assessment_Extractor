# Developer Notes

## Project Architecture

- **parser.py**  
  Responsible for reading and parsing DOCX documents. It identifies structured content such as headings, tables, and styled paragraphs to extract assessment questions, answers, and related metadata.  
  Key tasks include:  
  - Detecting and parsing "CONCEPT CHECK" styled tables.  
  - Extracting question and answer pairs with associated marks.  
  - Building structured pandas DataFrames for downstream processing.

- **exporter.py**  
  Manages exporting the extracted data into formatted Word documents. It replicates the original assessment layouts as closely as possible, including styles and table formatting.  
  Key tasks include:  
  - Transforming DataFrames into Word tables with correct styling.  
  - Supporting export options for different output formats (currently Word, future CSV/JSON).  
  - Managing page breaks, headers, and footers for exported documents.

- **utils.py**  
  Contains utility functions that support parsing and exporting processes. Includes text extraction helpers, style detection, and formatting functions.  
  Examples:  
  - Functions for safely extracting text from DOCX runs and paragraphs.  
  - Helpers for converting numeric marks and validating content formats.  
  - Logging and error handling helpers.

- **injector.py**  
  Handles injecting or merging processed content back into existing documents or templates.  
  Key tasks include:  
  - Inserting extracted questions and answers into predefined document templates.  
  - Managing placeholders and formatting consistency during injection.  
  - Supporting updates or replacements of document sections based on extracted data.

---

## Design Decisions

- **python-docx**  
  Chosen for its robust and straightforward API to manipulate DOCX files programmatically. It supports accessing paragraph styles and table content, which is crucial for this project.

- **pandas**  
  Used to organize extracted data into DataFrames, providing powerful, flexible data manipulation and easy export capabilities.

- **Modular Design**  
  Separation of parsing, exporting, injection, and utility logic encourages maintainability and easier testing.

- **Style-Based Extraction**  
  Reliance on consistent document styles (e.g., Heading 1, "CONCEPT CHECK" tables) to reliably identify relevant content.

---

## Coding Style

- Follow [PEP8](https://pep8.org/) guidelines strictly for readability and consistency.  
- Use meaningful variable and function names.  
- Include comprehensive docstrings on all public functions and classes using Google-style or NumPy-style conventions.  
- Inline comments where logic is complex or non-obvious.  
- Consistent error handling and logging to ease debugging.

---

## Extending the Project

- **Add New Export Formats**  
  Implement export to CSV, JSON, Excel, or even interactive HTML reports for better integration and usability.

- **Enhance Parser Capabilities**  
  - Support additional question styles and formats beyond "CONCEPT CHECK".  
  - Handle multi-part questions or nested answer structures.  
  - Include metadata extraction like assessment titles, versioning, or author info.

- **Improve Error Handling and Logging**  
  - Add detailed logs for every parsing step.  
  - Implement warnings for unsupported or malformed content.  
  - Provide user-friendly error messages and recovery options.

- **User Interface Enhancements**  
  - Develop a GUI file browser for selecting input/output files.  
  - Add progress bars or logs for long-running processes.

- **Integration and Automation**  
  - Add CLI flags for batch processing and automation.  
  - Integrate into CI/CD pipelines for continuous validation of assessment documents.

- **Testing and Documentation**  
  - Expand unit and integration test coverage for all modules.  
  - Maintain up-to-date developer documentation and usage examples.

---

## Additional Notes

- Maintain strict privacy and security when handling input documents; avoid committing sensitive data.  
- Keep dependencies up-to-date and document environment requirements.  
- Encourage code reviews and pair programming to ensure code quality and knowledge sharing.

---

*End of Developer Notes*
