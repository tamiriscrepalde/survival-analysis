"""Useful functions related to load datasets."""


import os

# import numpy as np
import pandas as pd

from .GoogleUtils import GoogleUtils
from .utils import read_file

# import re



os.chdir(os.path.dirname(__file__))


class DatasetLoader:
    """
    This class must be used to load all datasets used in the analysis.
    Inside the class, the dataset loading must be implemented as a method.
    It's also desired that pre-processing and loading be implemented in different class methods,
    respecting the SOLID design pattern.

    PS: You shold delete the example methods in this file
    """

    def __init__(self):
        self.env = os.getenv("ENV", "dev")
        self.google_utils = GoogleUtils()

    def load_example_costs_dataset(self) -> pd.DataFrame:
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ullamcorper leo ut dignissim
        vulputate. Nulla vulputate magna quam, a molestie augue consequat sed. Mauris sit amet velit
        eleifend, blandit metus eget, commodo ligula. Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Aliquam ornare sapien lorem. Phasellus maximus purus vel elit cursus, tempus vestibulum leo
        consectetur. Praesent consectetur euismod nisi, ac aliquam lectus imperdiet ac.

        Note:
            Do not include the `self` parameter in the ``Args`` section.
        """
        query = read_file("queries/bigquery_costs_by_user.sql")
        raw_dataset = self.google_utils.read_from_bq(query)
        df_pre_processed = self.pre_process_costs_dataset(raw_dataset)
        return df_pre_processed

    def pre_process_costs_dataset(self, df_costs: pd.DataFrame) -> pd.DataFrame:
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ullamcorper leo ut dignissim
        vulputate.
        Args:
            param1 (str): Description of `param1`.
        Returns:
            Lorem ipsum dolor sit amet
        """

        def format_user_name(df: pd.DataFrame) -> pd.DataFrame:
            """
            Suspendisse posuere venenatis augue, a rhoncus ante fringilla eget.
            Args:
                param1 (str): Description of `param1`.
            Returns:
                Lorem ipsum dolor sit amet
            """
            df[["name", "scope"]] = df.user.str.split(
                "@",
                expand=True,
            )
            df["is_service_account"] = df["scope"] != "hurb.com"
            return df

        def convert_dolar_cost(df: pd.DataFrame) -> pd.DataFrame:
            """
            Nulla massa leo, laoreet quis massa vitae, scelerisque accumsan nisi.
            Args:
                param1 (str): Description of `param1`.
            Returns:
                Lorem ipsum dolor sit amet
            """
            df["costs"] = df["costs"] * os.getenv("DOLAR_RATE", 5.3)
            return df

        df = df_costs.pipe(format_user_name).pipe(convert_dolar_cost)
        return df
