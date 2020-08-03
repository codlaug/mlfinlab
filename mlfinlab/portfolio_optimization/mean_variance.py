# pylint: disable=missing-module-docstring
import numpy as np
import pandas as pd
import cvxpy as cp
import matplotlib.pyplot as plt
from mlfinlab.portfolio_optimization.returns_estimators import ReturnsEstimators
from mlfinlab.portfolio_optimization.risk_estimators import RiskEstimators


class MeanVarianceOptimisation:
    """
    This class implements some classic mean-variance optimisation techniques for calculating the efficient frontier solutions.
    With the help of quadratic optimisers, users can generate optimal portfolios for different objective functions. Currently
    solutions to the following portfolios can be generated:

        1. Inverse Variance
        2. Maximum Sharpe
        3. Minimum Volatility
        4. Efficient Risk
        5. Maximum Return - Minimum Volatility
        6. Efficient Return
        7. Maximum Diversification
        8. Maximum Decorrelation
        9. Custom Objective Function
    """

    def __init__(self, calculate_expected_returns='mean', risk_free_rate=0.03):
        """
        Constructor.

        :param calculate_expected_returns: (str) The method to use for calculation of expected returns.
                                                 Currently supports: ``mean``, ``exponential``.
        """
        pass

    def allocate(self, asset_names=None, asset_prices=None, expected_asset_returns=None, covariance_matrix=None,
                 solution='inverse_variance', target_return=0.2, target_risk=0.01, risk_aversion=10, weight_bounds=None):
        # pylint: disable=invalid-name, too-many-branches
        """
        Calculate the portfolio asset allocations using the method specified.

        :param asset_names: (list) A list of strings containing the asset names.
        :param asset_prices: (pd.DataFrame) A dataframe of historical asset prices (daily close).
        :param expected_asset_returns: (list/np.array/pd.dataframe) A list of mean stock returns (mu).
        :param covariance_matrix: (pd.DataFrame/numpy matrix) User supplied covariance matrix of asset returns (sigma).
        :param solution: (str) The type of solution/algorithm to use to calculate the weights.
                               Supported solution strings - ``inverse_variance``, ``min_volatility``, ``max_sharpe``,
                               ``efficient_risk``, ``max_return_min_volatility``, ``max_diversification``, ``efficient_return``
                               and ``max_decorrelation``.
        :param target_return: (float) Target return of the portfolio.
        :param target_risk: (float) Target risk of the portfolio.
        :param risk_aversion: (float) Quantifies the risk averse nature of the investor - a higher value means
                                      more risk averse and vice-versa.
        :param weight_bounds: (dict/tuple) Can be either a single tuple of upper and lower bounds
                                           for all portfolio weights or a list of strings with each string representing
                                           an inequality on the weights. For e.g. to bound the weight of the 3rd asset
                                           pass the following weight bounds: ['weights[2] <= 0.3', 'weights[2] >= 0.1'].
        """
        pass

    def allocate_custom_objective(self, non_cvxpy_variables, cvxpy_variables, objective_function, constraints=None):
        # pylint: disable=eval-used, exec-used
        """
        Create a portfolio using custom objective and constraints.

        :param non_cvxpy_variables: (dict) A dictionary of variables to be used for providing the required input matrices and
                                           other inputs required by the user. The key of dictionary will be the variable name
                                           while the value can be anything ranging from a numpy matrix, list, dataframe or number.
        :param cvxpy_variables: (list) This is a list of cvxpy specific variables that will be initialised in the format required
                                       by cvxpy. For e.g. ["risk = cp.quad_form(weights, covariance)"] where you are initialising
                                       a variable named "risk" using cvxpy. Note that cvxpy is being imported as "cp", so be sure
                                       to refer to cvxpy as cp.
        :param custom_objective: (str)  A custom objective function. You need to write it in the form
                                        expected by cvxpy. The objective will be a single string, e.g. 'cp.Maximise(
                                        expected_asset_returns)'.
        :param constraints: (list) a list of strings containing the optimisation constraints. For e.g. ['weights >= 0', 'weights <= 1']
        """
        pass

    def get_portfolio_metrics(self):
        """
        Prints the portfolio metrics - return, risk and Sharpe Ratio.
        """
        pass

    def plot_efficient_frontier(self, covariance, expected_asset_returns, min_return=0, max_return=0.4,
                                risk_free_rate=0.05):
        # pylint: disable=broad-except
        """
        Plot the Markowitz efficient frontier.

        :param covariance: (pd.DataFrame) Covariance dataframe of asset returns.
        :param expected_asset_returns: (list/np.array/pd.dataframe) A list of mean stock returns (mu).
        :param min_return: (float) Minimum target return.
        :param max_return: (float) Maximum target return.
        :param risk_free_rate: (float) The rate of return for a risk-free asset.
        """
        pass
