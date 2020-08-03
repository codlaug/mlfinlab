"""
This module creates clustered subsets of features described in the paper Clustered Feature Importance (Presentation
Slides) by Dr. Marcos Lopez de Prado. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517595 and is also explained
in the book Machine Learning for Asset Managers Snippet 6.5.2 page 84.
"""

#Imports
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster
from statsmodels.regression.linear_model import OLS

from mlfinlab.clustering.onc import get_onc_clusters
from mlfinlab.codependence.codependence_matrix import get_dependence_matrix, get_distance_matrix


def get_feature_clusters(X: pd.DataFrame, dependence_metric: str, distance_metric: str = None,
                         linkage_method: str = None, n_clusters: int = None, critical_threshold: float = 0.0) -> list:
    """
    Machine Learning for Asset Managers
    Snippet 6.5.2.1 , page 85. Step 1: Features Clustering

    Gets clustered features subsets from the given set of features.

    :param X: (pd.DataFrame) Dataframe of features.
    :param dependence_metric: (str) Method to be use for generating dependence_matrix, either 'linear' or
                              'information_variation' or 'mutual_information' or 'distance_correlation'.
    :param distance_metric: (str) The distance operator to be used for generating the distance matrix. The methods that
                            can be applied are: 'angular', 'squared_angular', 'absolute_angular'. Set it to None if the
                            feature are to be generated as it is by the ONC algorithm.
    :param linkage_method: (str) Method of linkage to be used for clustering. Methods include: 'single', 'ward',
                           'complete', 'average', 'weighted', and 'centroid'. Set it to None if the feature are to
                           be generated as it is by the ONC algorithm.
    :param n_clusters: (int) Number of clusters to form. Must be less the total number of features. If None then it
                       returns optimal number of clusters decided by the ONC Algorithm.
    :param critical_threshold: (float) Threshold for determining low silhouette score in the dataset. It can any real number
                                in [-1,+1], default is 0 which means any feature that has a silhouette score below 0 will be
                                indentified as having low silhouette and hence requied transformation will be appiled to for
                                for correction of the same.
    :return: (list) Feature subsets.
    """
    pass
