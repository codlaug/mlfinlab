import numpy as np
import pandas as pd
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
from mlfinlab.portfolio_optimization.risk_estimators import RiskEstimators


class TIC:
    """
    This class implements the Theory-Implied Correlation (TIC) algorithm and the correlation matrix distance
    introduced by Herdin and Bonek. It is reproduced with modification from the following paper:
    `Marcos Lopez de Prado “Estimation of Theory-Implied Correlation Matrices”, (2019).
    <https://papers.ssrn.com/abstract_id=3484152>`_.
    """

    def __init__(self):
        """
        Initialize
        """

        pass

    def tic_correlation(self, tree_struct, corr_matrix, tn_relation, kde_bwidth=0.01):
        """
        Calculates the Theory-Implied Correlation (TIC) matrix.

        Includes three steps.

        In the first step, the theoretical tree graph structure of the assets is fit on the evidence
        presented by the empirical correlation matrix.

        The result of the first step is a binary tree (dendrogram) that sequentially clusters two elements
        together, while measuring how closely together the two elements are, until all elements are
        subsumed within the same cluster.

        In the second step, a correlation matrix is derived from the linkage object.

        Each cluster in the global linkage object is decomposed into two elements,
        which can be either atoms or other clusters. Then the off-diagonal correlation between two
        elements is calculated based on the distances between them.

        In the third step, the correlation matrix is de-noised.

        This is done by fitting the Marcenko-Pastur distribution to the eigenvalues of the matrix, calculating the
        maximum theoretical eigenvalue as a threshold and shrinking the eigenvalues higher than a set threshold.
        This algorithm is implemented in the RiskEstimators class.

        :param tree_struct: (pd.dataframe) The tree graph that represents the structure of the assets
        :param corr_matrix: (pd.dataframe) The empirical correlation matrix of the assets
        :param tn_relation: (float) Relation of sample length T to the number of variables N used to calculate the
                                    correlation matrix
        :param kde_bwidth: (float) The bandwidth of the kernel to fit KDE for de-noising the correlation matrix
                                   (0.01 by default)
        :return: (np.array) Theory-Implied Correlation matrix
        """

        pass

    @staticmethod
    def corr_dist(corr0, corr1):
        """
        Calculates the correlation matrix distance proposed by Herdin and Bonek.

        The distance obtained measures the orthogonality between the considered
        correlation matrices. If the matrices are equal up to a scaling factor,
        the distance becomes zero and one if they are different to a maximum
        extent.

        This can be used to measure to which extent the TIC matrix has blended
        theory-implied views (tree structure of the elements) with empirical
        evidence (correlation matrix).

        :param corr0: (pd.dataframe) First correlation matrix
        :param corr1: (pd.dataframe) Second correlation matrix
        :return: (float) Correlation matrix distance
        """

        pass
