"""Cleaner module for data cleaning utilities."""

import re
from concurrent.futures import ProcessPoolExecutor
import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean DataFrame column names by stripping whitespace and converting to lowercase.
    """
    return df.rename(columns=lambda x: x.strip().lower())

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame.
    """
    return df.drop_duplicates()

def clean_text_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Clean a specific text column in the DataFrame by removing extra spaces 
    and normalizing whitespace.
    """
    df[column] = df[column].astype(str).apply(
        lambda x: re.sub(r'\s+', ' ', x.strip())
    )
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all cleaning steps to the DataFrame.
    """
    df = clean_column_names(df)
    df = remove_duplicates(df)
    for col in df.select_dtypes(include='object').columns:
        df = clean_text_column(df, col)
    return df

def parallel_clean_data(dfs):
    """
    Clean multiple DataFrames in parallel.
    """
    with ProcessPoolExecutor() as executor:
        cleaned = list(executor.map(clean_data, dfs))
    return cleaned

def clean_question_text(text: str) -> str:
    """
    Remove instructional phrases and extra whitespace from question text.
    """
    patterns = [
        r"ASK participants:\s*",
        r"DISPLAY the question below on the PowerPoint Presentation\.\s*",
        r"MULTIPLE CHOICE QUESTIONS\s*"
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()

def _clean_row(row):
    """
    Clean the 'Questions' and 'Answer' fields in a row dictionary.
    """
    row["Questions"] = clean_question_text(str(row["Questions"]).strip())
    row["Answer"] = str(row["Answer"]).strip()
    return row

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the DataFrame by stripping whitespace and cleaning question text using
    multiprocessing.
    """
    required_columns = ["Questions", "Answer"]
    for column in required_columns:
        if column not in df.columns:
            raise KeyError(f"Missing required column: {column}")

    # Convert DataFrame to list of dicts for multiprocessing
    records = df.to_dict(orient="records")
    with ProcessPoolExecutor() as executor:
        cleaned_records = list(executor.map(_clean_row, records))
    return pd.DataFrame(cleaned_records)

def validate_columns(df: pd.DataFrame, required_columns: list) -> None:
    """
    Validate that all required columns are present in the DataFrame.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Missing required columns: {', '.join(missing_columns)}")
def clean_and_validate_data(df: pd.DataFrame, required_columns: list) -> pd.DataFrame:
    """
    Clean and validate the DataFrame, ensuring all required columns 
    are present and cleaned.
    """
    df = clean_data(df)
    validate_columns(df, required_columns)
    df = preprocess_data(df)
    return df
def clean_and_validate_data_parallel(dfs: list, required_columns: list) -> list:
    """
    Clean and validate multiple DataFrames in parallel, ensuring all required columns 
    are present and cleaned.
    """
    with ProcessPoolExecutor() as executor:
        cleaned_dfs = list(
            executor.map(lambda df: clean_and_validate_data(df, required_columns), dfs)
        )
    return cleaned_dfs
