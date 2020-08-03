

class CriticalLineAlgorithm:
    """
    This class implements the famous Critical Line Algorithm (CLA) for mean-variance portfolio optimisation. It is reproduced with
    modification from the following paper: `D.H. Bailey and M.L. Prado “An Open-Source Implementation of the Critical- Line
    Algorithm for Portfolio Optimization”,Algorithms, 6 (2013), 169-196. <http://dx.doi.org/10.3390/a6010169>`_.

    The Critical Line Algorithm is a famous portfolio optimisation algorithm used for calculating the optimal allocation weights
    for a given portfolio. It solves the optimisation problem with optimisation constraints on each weight - lower and upper
    bounds on the weight value. This class can compute multiple types of solutions:

    1. CLA Turning Points
    2. Minimum Variance
    3. Maximum Sharpe
    4. Efficient Frontier Allocations

    """

    def __init__(self, weight_bounds=(0, 1), calculate_expected_returns="mean"):
        """
        Initialise the storage arrays and some preprocessing.

        :param weight_bounds: (tuple) A tuple specifying the lower and upper bound ranges for the portfolio weights
        :param calculate_expected_returns: (str) The method to use for calculation of expected returns.
                                                 Currently supports ``mean`` and ``exponential``
        """
        pass

    def allocate(self,
                 asset_names=None,
                 asset_prices=None,
                 expected_asset_returns=None,
                 covariance_matrix=None,
                 solution="cla_turning_points",
                 resample_by=None):
        """
        Calculate the portfolio asset allocations using the method specified.

        :param asset_names: (list) List of strings containing the asset names
        :param asset_prices: (pd.Dataframe) Dataframe of historical asset prices (adj closed)
        :param expected_asset_returns: (list) List of mean stock returns (mu)
        :param covariance_matrix: (pd.Dataframe/numpy matrix) User supplied covariance matrix of asset returns
        :param solution: (str) Specifies the type of solution to compute. Supported strings: ``cla_turning_points``, ``max_sharpe``,
                               ``min_volatility``, ``efficient_frontier``
        :param resample_by: (str) Specifies how to resample the prices - weekly, daily, monthly etc.. Defaults to
                                  None for no resampling
        """

        pass
