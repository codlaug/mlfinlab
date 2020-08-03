"""
Implementation of an algorithm described in Yimou Li, David Turkington, Alireza Yazdani
'Beyond the Black Box: An Intuitive Approach to Investment Prediction with Machine Learning'
(https://jfds.pm-research.com/content/early/2019/12/11/jfds.2019.1.023)
"""
from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class AbstractModelFingerprint(ABC):
    """
    Model fingerprint constructor.

    This is an abstract base class for the RegressionModelFingerprint and ClassificationModelFingerprint classes.
    """

    def __init__(self):
        """
        Model fingerprint constructor.
        """

        pass

    def fit(self, model: object, X: pd.DataFrame, num_values: int = 50, pairwise_combinations: list = None) -> None:
        """
        Get linear, non-linear and pairwise effects estimation.

        :param model: (object) Trained model.
        :param X: (pd.DataFrame) Dataframe of features.
        :param num_values: (int) Number of values used to estimate feature effect.
        :param pairwise_combinations: (list) Tuples (feature_i, feature_j) to test pairwise effect.
        """
        pass

    def get_effects(self) -> Tuple:
        """
        Return computed linear, non-linear and pairwise effects. The model should be fit() before using this method.

        :return: (tuple) Linear, non-linear and pairwise effects, of type dictionary (raw values and normalised).
        """
        pass

    def plot_effects(self) -> plt.figure:
        """
        Plot each effect (normalized) on a bar plot (linear, non-linear). Also plots pairwise effects if calculated.

        :return: (plt.figure) Plot figure.
        """
        pass

    def _get_feature_values(self, X: pd.DataFrame, num_values: int) -> None:
        """
        Step 1 of the algorithm which generates possible feature values used in analysis.

        :param X: (pd.DataFrame) Dataframe of features.
        :param num_values: (int) Number of values used to estimate feature effect.
        """
        pass


class RegressionModelFingerprint(AbstractModelFingerprint):
    """
    Regression Fingerprint class used for regression type of models.
    """

    def __init__(self):
        """
        Regression model fingerprint constructor.
        """
        AbstractModelFingerprint.__init__(self)

    def _get_model_predictions(self, model, X_):
        """
        Abstract method _get_model_predictions implementation.

        :param model: (object) Trained model.
        :param X_: (np.array) Feature set.
        :return: (np.array) Predictions.
        """
        return model.predict(X_)


class ClassificationModelFingerprint(AbstractModelFingerprint):
    """
    Classification Fingerprint class used for classification type of models.
    """

    def __init__(self):
        """
        Classification model fingerprint constructor.
        """
        AbstractModelFingerprint.__init__(self)

    def _get_model_predictions(self, model, X_):
        """
        Abstract method _get_model_predictions implementation.

        :param model: (object) Trained model.
        :param X_: (np.array) Feature set.
        :return: (np.array) Predictions.
        """
        return model.predict_proba(X_)[:, 1]
