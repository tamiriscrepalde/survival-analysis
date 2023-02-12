import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('dark')
sns.set_palette(sns.color_palette("flare"))


def double_barplot(
    df: pd.DataFrame,
    column: str,
    consider_slice: int = None
) -> None:
    """Plot two barplots, one showing volume and other showing proportion.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
        consider_slice (int, optional): Used in a loc to slice the data. Defaults
            to None.
    """
    slice = df.groupby(column).count().order_date.reset_index()
    slice = slice.rename(
        columns={'order_date': 'volume'}
    ).sort_values('volume', ascending=False).reset_index(drop=True)
    slice['percent'] = slice.volume/slice.volume.sum()

    if consider_slice:
        slice = slice.loc[: consider_slice]

    _, ax = plt.subplots(2, sharex=True, figsize=(15, 8))

    sns.barplot(slice, x=column, y='volume', ax=ax[0])
    sns.barplot(slice, x=column, y='percent', ax=ax[1])

    plt.xticks(rotation=90)
    ax[0].set_title(f'Volume of cancelled orders by {column}.')
    ax[1].set_title(f'Percentage of cancelled orders by {column}.')
    plt.tight_layout()


def single_barplot(df: pd.DataFrame, column: str) -> None:
    """Plot a single barplot.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
    """
    slice = df.groupby(column).count().order_date.reset_index()
    slice = slice.rename(
        columns={'order_date': 'volume'}
    ).sort_values('volume', ascending=False).reset_index(drop=True)
    slice['percent'] = slice.volume/slice.volume.sum()

    plt.figure(figsize=(5, 6))

    sns.barplot(slice, x=column, y='percent')
    plt.title(f'Percentage of cancellations by {column}.')


def date_relationship(df: pd.DataFrame, column_min: str, column_max: str, new_column: str) -> None:
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


def single_histplot(df: pd.DataFrame, column: str) -> None:
    """Plot a single histplot.

    Args:
        df (pd.DataFrame): DataFrame with the data to be plot.
        column (str): Column to be plot.
    """
    plt.figure(figsize=(15, 8))

    sns.histplot(df[column], stat='proportion')

    plt.title(f'Proportion of {column} for order.')
    plt.xticks(df[column].unique())









# def vis_corr_matrix(df: pd.DataFrame) -> None:
#     """
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ullamcorper leo ut dignissim
#     vulputate.
#     Args:
#         param1 (str): Description of `param1`.
#     Returns:
#         Lorem ipsum dolor sit amet
#     """
#     corr = df.corr()
#     mask = np.zeros_like(corr, dtype=np.bool)
#     mask[np.triu_indices_from(mask)] = True
#     plt.figure(figsize=(13, 13))
#     cmap = sns.diverging_palette(220, 10, as_cmap=True)
#     with sns.axes_style("white"):
#         sns.heatmap(
#             corr,
#             cmap=cmap,
#             center=0,
#             mask=mask,
#             square=True,
#             linewidths=1.5,
#             cbar_kws={"shrink": 0.5},
#         )
