"""Exporter module for saving DataFrames to Word and Excel formats."""

import pandas as pd
from docx import Document  # Move import to top-level

def export_to_word(df: pd.DataFrame, output_path):
    """
    Export the DataFrame to a Word document.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        output_path (str or Path): The output file path.
    """
    doc = Document()
    table = doc.add_table(rows=1, cols=len(df.columns))
    hdr_cells = table.rows[0].cells
    for i, col in enumerate(df.columns):
        hdr_cells[i].text = str(col)

    for _, row in df.iterrows():
        row_cells = table.add_row().cells
        for i, item in enumerate(row):
            row_cells[i].text = str(item)

    doc.save(str(output_path))


def export_to_excel(df: pd.DataFrame, output_path):
    """
    Export the DataFrame to an Excel file.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        output_path (str or Path): The output file path.
    """
    df.to_excel(str(output_path), index=False)
