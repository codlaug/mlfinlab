"""
Explosiveness tests: Chow-Type Dickey-Fuller Test
"""
import pandas as pd
from mlfinlab.structural_breaks.sadf import get_betas
from mlfinlab.util import mp_pandas_obj


def get_chow_type_stat(series: pd.Series, min_length: int = 20, num_threads: int = 8, verbose: bool = True) -> pd.Series:
    """
    Multithread implementation of Chow-Type Dickey-Fuller Test, p.251-252

    :param series: (pd.Series) Series to test
    :param min_length: (int) Minimum sample length used to estimate statistics
    :param num_threads: (int): Number of cores to use
    :param verbose: (bool) Flag to report progress on asynch jobs
    :return: (pd.Series) Chow-Type Dickey-Fuller Test statistics
    """
    pass