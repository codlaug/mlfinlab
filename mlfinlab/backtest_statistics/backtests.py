

class CampbellBacktesting:
    """
    This class implements the Haircut Sharpe Ratios and Profit Hurdles algorithms described in the following paper:
    `Campbell R. Harvey and Yan Liu, Backtesting, (Fall 2015). Journal of Portfolio Management,
    2015 <https://papers.ssrn.com/abstract_id=2345489>`_; The code is based on the code provided by the authors of the paper.

    The Haircut Sharpe Ratios algorithm lets the user adjust the observed Sharpe Ratios to take multiple testing into account
    and calculate the corresponding haircuts. The haircut is the percentage difference between the original Sharpe ratio
    and the new Sharpe ratio.

    The Profit Hurdle algorithm lets the user calculate the required mean return for a strategy at a given level of
    significance, taking multiple testing into account.
    """

    def __init__(self, simulations=2000):
        """
        Set the desired number of simulations to make in Haircut Sharpe Ratios or Profit Hurdle algorithms.

        :param simulations: (int) Number of simulations
        """

        pass

    def haircut_sharpe_ratios(self, sampling_frequency, num_obs, sharpe_ratio, annualized,
                              autocorr_adjusted, rho_a, num_mult_test, rho):
        # pylint: disable=too-many-locals
        """
        Calculates the adjusted Sharpe ratio due to testing multiplicity.

        This algorithm lets the user calculate Sharpe ratio adjustments and the corresponding haircuts based on
        the key parameters of returns from the strategy. The adjustment methods are Bonferroni, Holm,
        BHY (Benjamini, Hochberg and Yekutieli) and the Average of them. The algorithm calculates adjusted p-value,
        adjusted Sharpe ratio and the haircut.

        The haircut is the percentage difference between the original Sharpe ratio and the new Sharpe ratio.

        :param sampling_frequency: (str) Sampling frequency ['D','W','M','Q','A'] of returns
        :param num_obs: (int) Number of returns in the frequency specified in the previous step
        :param sharpe_ratio: (float) Sharpe ratio of the strategy. Either annualized or in the frequency specified in the previous step
        :param annualized: (bool) Flag if Sharpe ratio is annualized
        :param autocorr_adjusted: (bool) Flag if Sharpe ratio was adjusted for returns autocorrelation
        :param rho_a: (float) Autocorrelation coefficient of returns at the specified frequency (if the Sharpe ratio
                              wasn't corrected)
        :param num_mult_test: (int) Number of other strategies tested (multiple tests)
        :param rho: (float) Average correlation among returns of strategies tested
        :return: (np.ndarray) Array with adjuted p-value, adjusted Sharpe ratio, and haircut as rows
                              for Bonferroni, Holm, BHY and average adjustment as columns
        """

        pass

    def profit_hurdle(self, num_mult_test, num_obs, alpha_sig, vol_anu, rho):
        """
        Calculates the required mean monthly return for a strategy at a given level of significance.

        This algorithm uses four adjustment methods - Bonferroni, Holm, BHY (Benjamini, Hochberg and Yekutieli)
        and the Average of them. The result is the Minimum Average Monthly Return for the strategy to be significant
        at a given significance level, taking into account multiple testing.

        This function doesn't allow for any autocorrelation in the strategy returns.

        :param num_mult_test: (int) Number of tests in multiple testing allowed (number of other strategies tested)
        :param num_obs: (int) Number of monthly observations for a strategy
        :param alpha_sig: (float) Significance level (e.g., 5%)
        :param vol_anu: (float) Annual volatility of returns(e.g., 0.05 or 5%)
        :param rho: (float) Average correlation among returns of strategies tested
        :return: (np.ndarray) Minimum Average Monthly Returns for
                              [Independent tests, Bonferroni, Holm, BHY and Average for Multiple tests]
        """
        pass
