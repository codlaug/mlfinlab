"""
This module contains class for ETF trick generation and futures roll function, described in Marcos Lopez de Prado's
book 'Advances in Financial Machine Learning' ETF trick class can generate ETF trick series either from .csv files
or from in memory pandas DataFrames
"""
import warnings
import pandas as pd
import numpy as np


class ETFTrick:
    """
    Contains logic of vectorised ETF trick implementation. Can used for both memory data frames (pd.DataFrame) and
    csv files. All data frames, files should be processed in a specific format, described in examples
    """

    def __init__(self, open_df, close_df, alloc_df, costs_df, rates_df=None, index_col=0):
        """
        Constructor

        Creates class object, for csv based files reads the first data chunk.

        :param open_df: (pd.DataFrame or string): open prices data frame or path to csv file,
         corresponds to o(t) from the book
        :param close_df: (pd.DataFrame or string): close prices data frame or path to csv file, corresponds to p(t)
        :param alloc_df: (pd.DataFrame or string): asset allocations data frame or path to csv file (in # of contracts),
         corresponds to w(t)
        :param costs_df: (pd.DataFrame or string): rebalance, carry and dividend costs of holding/rebalancing the
         position, corresponds to d(t)
        :param rates_df: (pd.DataFrame or string): dollar value of one point move of contract includes exchange rate,
         futures contracts multiplies). Corresponds to phi(t)
         For example, 1$ in VIX index, equals 1000$ in VIX futures contract value.
         If None then trivial (all values equal 1.0) is generated
        :param index_col: (int): positional index of index column. Used for to determine index column in csv files
        """

        pass

    def generate_trick_components(self, cache=None):
        """
        Calculates all etf trick operations which can be vectorised. Outputs multilevel pandas data frame.

        Generated components:
        'w': alloc_df
        'h_t': h_t/K value from ETF trick algorithm from the book. Which K to use is based on previous values and
            cannot be vectorised.
        'close_open': close_df - open_df
        'price_diff': close price differences
        'costs': costs_df
        'rate': rates_df

        :param cache: (dict of pd.DataFrames): dictionary which contains latest 2 rows of open, close, rates, alloc,
            costs, rates data
        :return: (pd.DataFrame): pandas data frame with columns in a format: component_1/asset_name_1,
            component_1/asset_name_2, ..., component_6/asset_name_n
        """
        pass

    def get_etf_series(self, batch_size=1e5):
        """
        External method which defines which etf trick method to use.

        :param: batch_size: Size of the batch that you would like to make use of
        :return: (pd.Series): pandas Series with ETF trick values starting from 1.0
        """
        pass

    def reset(self):
        """
        Re-inits class object. This methods can be used to reset file iterators for multiple get_etf_trick() calls.
        """
        pass


def get_futures_roll_series(data_df, open_col, close_col, sec_col, current_sec_col, roll_backward=False,
                            method='absolute'):
    """
    Function for generating rolling futures series from data frame of multiple futures.

    :param data_df: (pd.DataFrame): pandas DataFrame containing price info, security name and current active futures
     column
    :param open_col: (string): open prices column name
    :param close_col: (string): close prices column name
    :param sec_col: (string): security name column name
    :param current_sec_col: (string): current active security column name. When value in this column changes it means
     rolling
    :param roll_backward: (boolean): True for subtracting final gap value from all values
    :param method: (string): what returns user wants to preserve, 'absolute' or 'relative'
    :return (pd.Series): futures roll close price series
    """

    pass
