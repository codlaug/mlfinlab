"""
Volume classification methods (BVC and tick rule)
"""
import pandas as pd


def get_bvc_buy_volume(close: pd.Series, volume: pd.Series, window: int = 20) -> pd.Series:
    """
    Calculates the BVC buy volume

    :param close: (pd.Series): Close prices
    :param volume: (pd.Series): Bar volumes
    :param window: (int): Window for std estimation uses in BVC calculation
    :return: (pd.Series) BVC buy volume
    """
    pass
