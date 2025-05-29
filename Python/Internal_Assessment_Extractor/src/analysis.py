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
