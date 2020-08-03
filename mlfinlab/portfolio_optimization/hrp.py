
class HierarchicalRiskParity:
    """
    This class implements the Hierarchical Risk Parity algorithm mentioned in the following paper: `López de Prado, Marcos,
    Building Diversified Portfolios that Outperform Out-of-Sample (May 23, 2016). Journal of Portfolio Management,
    2016 <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678>`_; The code is reproduced with modification from his book:
    Advances in Financial Machine Learning, Chp-16
    By removing exact analytical approach to the calculation of weights and instead relying on an approximate
    machine learning based approach (hierarchical tree-clustering), Hierarchical Risk Parity produces weights which are stable to
    random shocks in the stock-market. Moreover, previous algorithms like CLA involve the inversion of covariance matrix which is
    a highly unstable operation and tends to have major impacts on the performance due to slight changes in the covariance matrix.
    By removing dependence on the inversion of covariance matrix completely, the Hierarchical Risk Parity algorithm is fast,
    robust and flexible.
    """

    def __init__(self):
        pass

    def allocate(self,
                 asset_names=None,
                 asset_prices=None,
                 asset_returns=None,
                 covariance_matrix=None,
                 distance_matrix=None,
                 side_weights=None,
                 linkage='single'):
        """
        Calculate asset allocations using HRP algorithm.

        :param asset_names: (list) A list of strings containing the asset names
        :param asset_prices: (pd.Dataframe) A dataframe of historical asset prices (daily close)
                                            indexed by date
        :param asset_returns: (pd.Dataframe/numpy matrix) User supplied matrix of asset returns
        :param covariance_matrix: (pd.Dataframe/numpy matrix) User supplied covariance matrix of asset returns
        :param distance_matrix: (pd.Dataframe/numpy matrix) User supplied distance matrix
        :param side_weights: (pd.Series/numpy matrix) With asset_names in index and value 1 for Buy, -1 for Sell
                                                      (default 1 for all)
        :param linkage: (string) Type of linkage used for Hierarchical Clustering. Supported strings - ``single``,
                                 ``average``, ``complete``, ``ward``.
        """

        pass

    def plot_clusters(self, assets):
        """
        Plot a dendrogram of the hierarchical clusters.

        :param assets: (list) Asset names in the portfolio
        :return: (dict) Dendrogram
        """

        pass
