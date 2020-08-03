"""
Implementation of Chu-Stinchcombe-White test
"""


def get_chu_stinchcombe_white_statistics(series: pd.Series, test_type: str = 'one_sided',
                                         num_threads: int = 8, verbose: bool = True) -> pd.Series:
    """
    Multithread Chu-Stinchcombe-White test implementation, p.251

    :param series: (pd.Series) Series to get statistics for
    :param test_type: (str): Two-sided or one-sided test
    :param num_threads: (int) Number of cores
    :param verbose: (bool) Flag to report progress on asynch jobs
    :return: (pd.Series) Statistics
    """
    pass
