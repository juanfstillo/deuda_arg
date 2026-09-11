"""Reusable data cleaning helpers for the project."""

import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Run standard cleaning steps on a dataframe."""
    # Example basic steps; expand as needed
    df = df.copy()
    df.columns = df.columns.str.strip()
    df = df.dropna(how="all")
    return df
