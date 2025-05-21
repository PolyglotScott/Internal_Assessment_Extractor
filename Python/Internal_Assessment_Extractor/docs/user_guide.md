# Troubleshooting Guide

This guide helps diagnose and resolve common issues encountered while using the **internall_assessment_extractor** project.

---

## Common Issues & Solutions

### 1. Module Not Found or Import Errors

**Symptoms:**  
- `ModuleNotFoundError` when running scripts  
- Python cannot locate installed packages

**Possible Causes:**  
- Dependencies not installed  
- Running the script outside the virtual environment  
- Incorrect Python version

**Solutions:**  
- Ensure you have activated your virtual environment:  
  - On macOS/Linux: `source venv/bin/activate`  
  - On Windows: `venv\Scripts\activate`  
- Install dependencies with:  
  `pip install -r requirements.txt`  
- Confirm Python version is 3.8 or higher:  
  `python --version`  
- If using multiple Python versions, specify the correct interpreter explicitly:  
  `python3.11 src/parser.py --input path/to/file.docx`

---

### 2. Parsing Errors or Unexpected Output

**Symptoms:**  
- Script runs but extracts incomplete or incorrect data  
- Errors related to document structure, missing elements, or attributes

**Possible Causes:**  
- Input DOCX file does not conform to expected style or format  
- Unexpected formatting or missing style tags in the document  
- Tables or headings formatted differently than assumed

**Solutions:**  
- Verify the input document matches the expected formatting conventions, especially:  
  - Use of specific heading styles (e.g., Heading 1, Heading 2)  
  - Tables marked with correct styles for questions/answers  
- Open the document in Microsoft Word and check the style pane for applied styles  
- Test with a simplified or sample DOCX that meets all formatting requirements  
- Review logs or error messages for clues, and add debugging prints in `parser.py` if needed

---

### 3. Exported Document Formatting Issues

**Symptoms:**  
- Exported Word document has misaligned tables or styles  
- Missing or incorrect text formatting in output files

**Possible Causes:**  
- Limitations in python-docx formatting capabilities  
- Differences in template or style references  
- Export script not updated to handle all formatting cases

**Solutions:**  
- Review and customize styles defined in `exporter.py` or related utilities  
- Manually inspect and adjust templates in the `templates/` folder if used  
- Use Microsoft Word’s style inspector to compare expected vs actual styles  
- Update the exporter script to handle new formatting cases as needed

---

### 4. Performance Issues on Large Documents

**Symptoms:**  
- Long processing times or script hangs on large input files  
- High memory usage or crashes

**Possible Causes:**  
- Inefficient parsing or data handling logic  
- Large, complex DOCX files with many images or embedded objects

**Solutions:**  
- Profile script performance and identify bottlenecks (e.g., using `cProfile`)  
- Break large documents into smaller chunks before processing  
- Optimize loops and data operations in `parser.py` and related code  
- Avoid loading unnecessary parts of the document (e.g., images) if not needed

---

### 5. Git and Version Control Issues

**Symptoms:**  
- Private files accidentally committed  
- Sensitive data exposed in public repository  
- Merge conflicts or branch issues

**Possible Causes:**  
- `.gitignore` not properly configured  
- Committing files without checking contents

**Solutions:**  
- Ensure `.gitignore` excludes `input/`, `output/`, and any environment files  
- Use `git status` frequently to verify staged files  
- For sensitive data removed accidentally, consider using git filter-branch or tools like BFG Repo-Cleaner  
- Maintain clear branch naming and commit message conventions

---

## General Debugging Tips

- Add print statements or logging in your Python scripts to trace data flow  
- Use smaller test files during development  
- Read error tracebacks carefully for line numbers and error types  
- Consult Python package documentation for usage questions (e.g., python-docx)  
- Reach out via GitHub issues or email if you suspect bugs or need help

---

## Getting Help

If you continue experiencing issues, please:

- Open a GitHub issue in the repository with a detailed description  
- Include sample input files (if possible and non-sensitive)  
- Provide error messages and relevant environment details (OS, Python version)

---

*This troubleshooting guide will be updated regularly as new issues and solutions arise.*
