import unicodedata
from typing import List

import pandas as pd


def treat_accom_type(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Preprocess the accommodation_type column to reduce cardinality.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        column (str): Column to be preprocessed.

    Returns:
        pd.DataFrame: DataFrame with the preprocessed column.
    """
    df[column] = df[column].str.lower()
    df[column] = df[column].str.replace('.', '', regex=False)
    df[column] = df[column].apply(lambda x: ''.join(
        c for c in unicodedata.normalize('NFD', x)
        if unicodedata.category(c) != 'Mn')
        )

    df.loc[df[column].str.contains(','), 'accommodation_type'] = 'multiple'
    df.loc[df[column].str.contains('individual'), 'accommodation_type'] = 'individual'
    df.loc[df[column].str.contains('dupl'), 'accommodation_type'] = 'duplo'
    df.loc[df[column].str.contains('tripl'), 'accommodation_type'] = 'triplo'
    df.loc[df[column].str.contains('quadrupl'), 'accommodation_type'] = 'quadruplo'

    return df


def convert_to_datetime(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Convert a list of columns into datetime.

    Args:
        df (pd.DataFrame): DataFrame containing the data to be converted.
        columns (List[str]): List of columns to convert.

    Returns:
        pd.DataFrame: DataFrame containing the columns converted.
    """
    for column in columns:
        df[column] = pd.to_datetime(df[column])
    return df


def convert_to_int(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Convert a list of columns into integer.

    Args:
        df (pd.DataFrame): DataFrame containing the data to be converted.
        columns (List[str]): List of columns to convert.

    Returns:
        pd.DataFrame: DataFrame containing the columns converted.
    """
    for column in columns:
        df[column] = df[column].astype(int)
    return df
