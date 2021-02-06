"""
Sally Poon; A01232177
Date Completed: February 5th, 2021

This module is a unit test for lottery.py, demonstrating that fulfills program requirements.

Required imports of TestCase from unittest and patch from unittest.mock
in addition to lottery from lottery.py.
"""

from unittest import TestCase
from unittest.mock import patch

import lottery as lottery


class TestLottery(TestCase):

    def test_lottery_correct_length(self):
        # Test that there are 6 numbers
        expected = 6
        actual = len(lottery.lottery())
        self.assertEqual(expected, actual)

    def test_lottery_element_within_range(self):
        # Test that each element in lottery() list is [1, 49]
        expected = range(1, 50)
        actual_lottery = lottery.lottery()
        for number in actual_lottery:
            actual_number = number
            self.assertIn(actual_number, expected)

    def test_lottery_sorted(self):
        # Test that lottery() list is sorted from least to greatest
        actual = lottery.lottery()
        expected = sorted(actual)
        self.assertTrue(expected, actual)

    def test_lottery_unique(self):
        # Test that each number in lottery() is unique
        actual_lottery = lottery.lottery()
        for number in actual_lottery:
            expected_distinct_count = 1
            actual_count = actual_lottery.count(number)
            self.assertEqual(expected_distinct_count, actual_count)

    @patch('lottery.sample', return_value=[49, 34, 28, 11, 9, 1])
    def test_lottery_single_lottery(self, mock_randomsample):
        # Patch random.sample, test logic of function
        actual = lottery.lottery()
        self.assertEqual(actual, [1, 9, 11, 28, 34, 49])

