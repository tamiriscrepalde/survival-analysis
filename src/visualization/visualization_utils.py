import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import src.utils as utils

sns.set_style('dark')
sns.set_palette(sns.color_palette("flare"))


def double_barplot(
    df: pd.DataFrame,
    column: str,
    consider_slice: int = None,
    **kwargs
) -> None:
    """Plot two barplots, one showing volume and other showing proportion.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
        consider_slice (int, optional): Used in a loc to slice the data. Defaults
            to None.
    """
    if 'hue' in kwargs.keys():
        slice = utils.group_data(df, [column, kwargs['hue']])
    else:
        slice = utils.group_data(df, [column])

    if consider_slice:
        slice = slice.loc[: consider_slice]

    _, ax = plt.subplots(2, sharex=True, figsize=(15, 8))

    sns.barplot(slice, x=column, y='volume', ax=ax[0], **kwargs)
    sns.barplot(slice, x=column, y='percent', ax=ax[1], **kwargs)

    plt.xticks(rotation=90)
    ax[0].set_title(f'Volume of cancelled orders by {column}.')
    ax[1].set_title(f'Percentage of cancelled orders by {column}.')
    plt.tight_layout()


def single_barplot(df: pd.DataFrame, column: str, **kwargs) -> None:
    """Plot a single barplot.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
    """
    if 'hue' in kwargs.keys():
        slice = utils.group_data(df, [column, kwargs['hue']])
    else:
        slice = utils.group_data(df, [column])

    plt.figure(figsize=(5, 6))

    sns.barplot(slice, x=column, y='percent', **kwargs)
    plt.title(f'Percentage of cancellations by {column}.')


def date_relationship(
    df: pd.DataFrame,
    column_min: str,
    column_max: str,
    new_column: str
) -> None:
    """Plot the difference between two datetime columns.

    Args:
        df (pd.DataFrame): DataFrame containing the data to be plot.
        column_min (str): Datetime column that represents the first event.
        column_max (str): Datetime column that represents the last event.
        new_column (str): Name of the new column.
    """
    df_dates = pd.DataFrame()
    df_dates[new_column] = (df[column_max] - df[column_min])
    df_dates[f'{new_column}_days'] = df_dates[new_column].astype('timedelta64[D]').astype(int)
    df_dates[f'{new_column}_months'] = df_dates[new_column].astype('timedelta64[M]').astype(int)

    for col in [f'{new_column}_days', f'{new_column}_months']:
        plt.figure(figsize=(15, 8))

        sns.histplot(df_dates[col], kde=True, stat='proportion')

        t = col.split('_')[-1:][0]
        plt.title(f'Volume of cancelled orders by {new_column} in {t}.')
        plt.tight_layout()


def single_histplot(
    df: pd.DataFrame,
    column: str,
    consider_slice: int = None,
    **kwargs
) -> None:
    """Plot a single histplot.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
    """
    plt.figure(figsize=(15, 8))

    if consider_slice:
        sns.histplot(df, x=column, stat='proportion', **kwargs)
    else:
        sns.histplot(df, x=column, stat='proportion', **kwargs)

    plt.xticks(rotation=90)
    plt.title(f'Proportion of {column} for order.')
    plt.xticks(df[column].unique())
