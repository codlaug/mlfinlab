

class TailSetLabels:
    """
    Tail set labels are a classification labeling technique introduced in the following paper: Nonlinear support vector
    machines can systematically identify stocks with high and low future returns. Algorithmic Finance, 2(1), pp.45-58.

    A tail set is defined to be a group of stocks whose volatility-adjusted return is in the highest or lowest
    quantile, for example the highest or lowest 5%.

    A classification model is then fit using these labels to determine which stocks to buy and sell in a long / short
    portfolio.
    """

    def __init__(self, prices, n_bins, vol_adj=None, window=None):
        """
        :param prices: (pd.DataFrame) Asset prices.
        :param n_bins: (int) Number of bins to determine the quantiles for defining the tail sets. The top and
                        bottom quantiles are considered to be the positive and negative tail sets, respectively.
        :param vol_adj: (str) Whether to take volatility adjusted returns. Allowable inputs are ``None``,
                        ``mean_abs_dev``, and ``stdev``.
        :param window: (int) Window period used in the calculation of the volatility adjusted returns, if vol_adj is not
                        None. Has no impact if vol_adj is None.
        """
        pass

    def get_tail_sets(self):
        """
        Computes the tail sets (positive and negative) and then returns a tuple with 3 elements, positive set, negative
        set, full matrix set.

        The positive and negative sets are each a series of lists with the names of the securities that fall within each
        set at a specific timestamp.

        For the full matrix a value of 1 indicates the volatility adjusted returns were in the top quantile, a value of
        -1 for the bottom quantile.
        :return: (tuple) positive set, negative set, full matrix set.
        """
        pass
