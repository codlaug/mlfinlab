"""
Tests Online Portfolio Selection.
"""

from unittest import TestCase
import os
import numpy as np
import pandas as pd
from mlfinlab.online_portfolio_selection import OLPS


class TestOLPS(TestCase):
    # pylint: disable=too-many-public-methods
    # pylint: disable=unsubscriptable-object
    """
    Tests different functions of the OLPS class.
    """

    def setUp(self):
        """
        Sets the file path for the tick data csv.
        """
        # Set project path to current directory.
        project_path = os.path.dirname(__file__)
        # Add new data path to match stock_prices.csv data.
        data_path = project_path + '/test_data/stock_prices.csv'
        # Read csv, parse dates, and drop NaN.
        self.data = pd.read_csv(data_path, parse_dates=True, index_col="Date").dropna(axis=1)

    def test_olps_solution(self):
        """
        Test the calculation of OLPS weights.
        """
        # Initialize OLPS.
        olps = OLPS()
        # Allocates asset prices to OLPS.
        olps.allocate(self.data)
        # Create np.array of all_weights.
        all_weights = np.array(olps.all_weights)
        # Check if all weights sum to 1.
        for i in range(all_weights.shape[0]):
            weights = all_weights[i]
            assert (weights >= 0).all()
            assert len(weights) == self.data.shape[1]
            np.testing.assert_almost_equal(np.sum(weights), 1)

    def test_olps_weight_mismatch(self):
        """
        Tests that the user inputted weights have matching dimensions as the data's dimensions.
        """
        # Initialize OLPS.
        olps1 = OLPS()
        # Raise error if weight does not match data.shape[1].
        with self.assertRaises(ValueError):
            olps1.allocate(self.data, weights=[1])

    def test_olps_weight_incorrect_sum(self):
        """
        Tests ValueError if the user inputted weights do not sum to one.
        """
        with self.assertRaises(AssertionError):
            # Initialize OLPS.
            olps2 = OLPS()
            # Initialize weights that do not sum to 1.
            weight = np.zeros(self.data.shape[1])
            weight[0], weight[1] = 0.4, 0.4
            # Running allocate will raise ValueError.
            olps2.allocate(self.data, weight)

    def test_olps_incorrect_data(self):
        """
        Tests ValueError if the user inputted data is not a dataframe.
        """
        with self.assertRaises(ValueError):
            # Initialize OLPS.
            olps3 = OLPS()
            # Running alloate will raise ValueError.
            olps3.allocate(self.data.values)

    def test_olps_index_error(self):
        """
        Tests ValueError if the passing dataframe is not indexed by date.
        """
        # Initialize OLPS.
        olps4 = OLPS()
        # Reset index.
        data = self.data.reset_index()
        with self.assertRaises(ValueError):
            # Running allocate will raise ValueError.
            olps4.allocate(data)

    def test_user_weight(self):
        """
        Tests that users can input their own weights for OLPS.
        """
        # Initialize user inputted weights.
        weight = np.zeros(self.data.shape[1])
        weight[0] = 1
        # Initialize OLPS.
        olps5 = OLPS()
        # Allocates asset prices to OLPS.
        olps5.allocate(self.data, weights=weight)
        # Create np.array of all_weights.
        all_weights = np.array(olps5.all_weights)
        # Check if all weights sum to 1.
        for i in range(all_weights.shape[0]):
            weights = all_weights[i]
            assert (weights >= 0).all()
            assert len(weights) == self.data.shape[1]
            np.testing.assert_almost_equal(np.sum(weights), 1)

    def test_uniform_weight(self):
        """
        Tests that uniform weights return equal allocation of weights.
        """
        # Initialize OLPS.
        olps6 = OLPS()
        # Allocates asset prices to OLPS.
        olps6.allocate(self.data)
        # Calculate uniform weights.
        olps6_uni_weight = olps6.uniform_weight()
        # Calculated weights should be equal.
        np.testing.assert_almost_equal(olps6_uni_weight, np.array(olps6.all_weights)[0])

    def test_normalize(self):
        """
        Tests that weights sum to 1.
        """
        # Initialize OLPS.
        olps7 = OLPS()
        # Allocates asset prices to OLPS.
        olps7.allocate(self.data)
        # Test normalization on a random weight.
        random_weight = np.ones(3)
        # Use method to normalize random_weight.
        normalized_weight = olps7.normalize(random_weight)
        # Compare normalized value and manually calculated value.
        np.testing.assert_almost_equal(normalized_weight, random_weight / 3)

    def test_simplex_projection(self):
        """
        Tests edge cases where the inputted weights already satisfy the simplex requirements.
        """
        # Initialize OLPS.
        olps8 = OLPS()
        # Allocates asset prices to OLPS.
        olps8.allocate(self.data)
        # Initialize uniform weights.
        weights = olps8.uniform_weight()
        # Project uniform weights to simplex domain.
        simplex_weights = olps8.simplex_projection(weights)
        # The two weights should be the same value.
        np.testing.assert_almost_equal(weights, simplex_weights)
