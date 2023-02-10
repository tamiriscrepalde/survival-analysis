"""Useful general functions."""

from typing import List

import pandas as pd


def read_file(file_path: str) -> str:
    """Read file and returns its content.

    Args:
        file_path (str): Path of the file.

    Returns:
        str: File's content.
    """
    file = open(file_path, "r", encoding="utf-8")
    content = file.read()
    file.close()

    return content


def convert_to_boolean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Converts a column to boolean.

    Args:
        df (pd.DataFrame): DataFrame containing column of interest.
        column (str): Column to be converted.

    Returns:
        pd.DataFrame: DataFrame containing converted column.
    """
    df.loc[df[column].isna(), column] = False
    df.loc[~df[column].isna(), column] = True

    return df


def create_date_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        column (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df_dates = pd.DataFrame()
    for column in columns:
        df_dates[f'{column}_year'] = df[column].dt.year
        df_dates[f'{column}_month'] = df[column].dt.month

    return df_dates
