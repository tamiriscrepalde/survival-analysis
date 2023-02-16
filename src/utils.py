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


def convert_to_boolean(
    df: pd.DataFrame,
    column: str,
    new_column_name: str = None,
    consider_column_value: str = None
) -> pd.DataFrame:
    """Convert a column to boolean.

    Args:
        df (pd.DataFrame): DataFrame containing column of interest.
        column (str): Column to be converted.

    Returns:
        pd.DataFrame: DataFrame containing converted column.
    """
    if new_column_name is None:
        new_column_name = column

    if consider_column_value:
        df.loc[df[column] == consider_column_value, new_column_name] = True
        df.loc[df[column] != consider_column_value, new_column_name] = False
        return df

    df.loc[~df[column].isna(), new_column_name] = True
    df.loc[df[column].isna(), new_column_name] = False

    return df


def create_date_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Create year and month columns for a list of columns.

    Args:
        df (pd.DataFrame): DataFrame containing the data to be used.
        column (List[str]): List of columns to be used.

    Returns:
        pd.DataFrame: DataFrame containing the new columns.
    """
    df_dates = pd.DataFrame()
    for column in columns:
        df_dates[f'{column}_year'] = df[column].dt.year
        df_dates[f'{column}_month'] = df[column].dt.month

    return df_dates


def group_data(df: pd.DataFrame, group: List[str]) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        group (List[str]): _description_

    Returns:
        pd.DataFrame: _description_
    """
    grouped = df.groupby(group).count().iloc[:, -1].reset_index()
    grouped = grouped.rename(
        columns={grouped.iloc[:, -1].name: 'volume'}
    ).sort_values('volume', ascending=False).reset_index(drop=True)
    grouped['percent'] = grouped.volume/grouped.volume.sum()

    return grouped
