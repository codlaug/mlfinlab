

class HierarchicalEqualRiskContribution:
    """
    This class implements the Hierarchical Equal Risk Contribution (HERC) algorithm and it's extended components mentioned in the
    following papers: `Raffinot, Thomas, The Hierarchical Equal Risk Contribution Portfolio (August 23,
    2018). <https://ssrn.com/abstract=3237540>`_; and `Raffinot, Thomas, Hierarchical Clustering Based Asset Allocation (May 2017)
    <https://ssrn.com/abstract=2840729>`_;

    While the vanilla Hierarchical Risk Parity algorithm uses only the variance as a risk measure for assigning weights, the HERC
    algorithm proposed by Raffinot, allows investors to use other risk metrics like Standard Deviation, Expected Shortfall and
    Conditional Drawdown at Risk.
    """

    def __init__(self, confidence_level=0.05):
        """
        Initialise.

        :param confidence_level: (float) The confidence level (alpha) used for calculating expected shortfall and conditional
                                         drawdown at risk.
        """

        pass

    def allocate(self, asset_names=None, asset_prices=None, asset_returns=None, covariance_matrix=None,
                 risk_measure='equal_weighting', linkage='ward', optimal_num_clusters=None):
        """
        Calculate asset allocations using the Hierarchical Equal Risk Contribution algorithm.

        :param asset_names: (list) A list of strings containing the asset names.
        :param asset_prices: (pd.DataFrame) A dataframe of historical asset prices (daily close)
                                            indexed by date.
        :param asset_returns: (pd.DataFrame/numpy matrix) User supplied matrix of asset returns.
        :param covariance_matrix: (pd.DataFrame/numpy matrix) User supplied covariance matrix of asset returns.
        :param risk_measure: (str) The metric used for calculating weight allocations. Supported strings - ``equal_weighting``,
                                   ``variance``, ``standard_deviation``, ``expected_shortfall``, ``conditional_drawdown_risk``.
        :param linkage: (str) The type of linkage method to use for clustering. Supported strings - ``single``, ``average``,
                              ``complete``, ``ward``.
        :param optimal_num_clusters: (int) Optimal number of clusters for hierarchical clustering.
        """

        pass

    def plot_clusters(self, assets):
        """
        Plot a dendrogram of the hierarchical clusters.

        :param assets: (list) Asset names in the portfolio
        :return: (dict) Dendrogram
        """
        pass
