# Troubleshooting Guide

## Common Issues

### 1. ModuleNotFoundError or ImportError
- **Symptom:** Python throws errors like `ModuleNotFoundError` for packages such as `python-docx` or `pandas`.
- **Solution:**  
  - Verify you have installed all required dependencies:  
    ```bash
    pip install -r requirements.txt
    ```  
  - Ensure you are using the correct Python environment (e.g., activate your virtual environment).  
  - Confirm Python version is 3.8 or above (`python --version`).

### 2. Parsing Errors or Missing Data Extraction
- **Symptom:** The parser script runs without crashing but produces empty or incomplete results.
- **Causes and Solutions:**  
  - **Incorrect DOCX formatting or styles:** The parser depends on consistent styles like "Heading 1", "CONCEPT CHECK" tables, and specific paragraph styles.  
    - Open your DOCX file in Word and verify that the expected styles are applied properly.  
    - Avoid manual direct formatting; use Word’s Styles pane to assign styles.  
  - **Unsupported document structure:** If your input DOCX deviates significantly from the expected format (e.g., different table layouts, missing headings), the parser might fail to recognize content.  
    - Consider modifying or extending the parser logic in `src/parser.py` to handle your document’s structure.  
  - **Corrupted or locked DOCX file:** Make sure the file is not corrupted or open in another program during parsing.

### 3. Exporting Issues
- **Symptom:** Exported Word documents are malformed or missing content.
- **Possible Causes:**  
  - DataFrame used for export might be empty or improperly structured. Verify the parsing output before export.  
  - Formatting issues in exporter code; check for recent changes in `src/exporter.py`.  
- **Solutions:**  
  - Run the parser first and inspect the DataFrame preview printed in the console.  
  - Add logging in `exporter.py` to identify where formatting may break.  
  - Test export with sample data to isolate issues.

### 4. Injector Failures
- **Symptom:** Content injection does not update the target document or inserts incorrectly formatted content.
- **Solutions:**  
  - Verify the injector is pointed to the correct template and that placeholders match expected tags.  
  - Review `src/injector.py` for error messages or exceptions.  
  - Test injection with minimal input data to confirm baseline functionality.

### 5. Environment and Execution Issues
- **Symptom:** Scripts hang, run slowly, or behave inconsistently.
- **Suggestions:**  
  - Ensure no conflicting Python versions or environment variables.  
  - Use a fresh virtual environment for testing.  
  - Confirm adequate system resources and permissions to read/write files.

---

## Debugging Tips

- Use verbose logging by temporarily adding `print()` statements or Python’s `logging` module calls inside the parser, exporter, and injector scripts.  
- Test with minimal, well-structured DOCX files before scaling up to larger documents.  
- Break down the workflow: parse → inspect data → export → inject to isolate problematic steps.  
- Use a Python debugger (e.g., `pdb`) to step through the code if needed.

---

## Getting Help

- **GitHub Issues:** Open a detailed issue at  
  [https://github.com/PolyglotScott/internal_assessment_extractor/issues](https://github.com/PolyglotScott/internal_assessment_extractor/issues)  
  Include sample input (if non-sensitive), error messages, and steps to reproduce.

- **Email Support:**  
  scott.maxwell.polyglot@gmail.com

- **Community:** Consider posting questions with relevant tags on Stack Overflow or Python forums if general issues arise.

---

## Best Practices

- Always keep backups of original DOCX files before processing.  
- Regularly update your dependencies to avoid compatibility issues.  
- Document any custom modifications you make to parsing/exporting logic for easier troubleshooting later.

---

*End of Troubleshooting Guide*
