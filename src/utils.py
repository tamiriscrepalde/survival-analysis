"""Useful general functions."""

import pandas as pd


def read_file(file_path: str) -> str:
    """Read file and returns its content.

    Args:
        file_path (str): Path of the file.

    Returns:
        str: File's content.
    """
    file = open(file_path, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    return content


def convert_to_boolean(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Converts a column to boolean.

    Args:
        df (pd.DataFrame): DataFrame containing column of interest.
        col (str): Column to be converted.

    Returns:
        pd.DataFrame: DataFrame containing converted column.
    """
    df.loc[df[col].isna(), col] = False
    df.loc[~df[col].isna(), col] = True

    return df
