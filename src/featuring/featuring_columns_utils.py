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
    df.loc[df[column].str.contains('1|individual'), 'accommodation_type'] = 'single'
    df.loc[df[column].str.contains('2|dupl|dbl'), 'accommodation_type'] = 'double'
    df.loc[df[column].str.contains('3|tripl'), 'accommodation_type'] = 'triple'
    df.loc[df[column].str.contains('4|quadrupl'), 'accommodation_type'] = 'quadruple'

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


def anonymize_data(
    df: pd.DataFrame,
    columns: List[str],
    type_: str
) -> pd.DataFrame:
    """Anonymize the data based on number of unique elements.

    Args:
        df (pd.DataFrame): DataFrame containing the data to be anonymize.
        columns (List[str]): Columns to be anonymize.
        type_ (str): Type of data to be anonymize.

    Returns:
        pd.DataFrame: DataFrame containing the anonymized data.
    """
    for column in columns:
        dict_ = {
            loc_: f'{type_}_{i+1}' for i, loc_ in enumerate(df[column].unique())
        }
        df[column] = df[column].map(dict_)

    return df
