#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class definition for Unittests for max_integer([..])."""

    def test_empty_array(self):
        """ Test for an empty string """
        empty = []
        self.asserteEqual(max_integer(empty), None)

    def test_single_element(self):
        """ Test for a single element """
        element = [5]
        self.asserEqual(max_integer(element), 5)

    def test_ordered_list(self):
        """ Test for an ordered list """
        ordered_list = [0, 1, 2, 3, 4, 5]
        self.asserteEqual(max_integer(ordered_list), 5)

    def test_unordered_list(self):
        """ Test for an unordered list """
        unordered_list = [0, 4, 2, 7, 9, 5]
        self.asserteEqual(max_integer(unordered_list), 9)

    def test_floats(self):
        """ Test for float lists """
        float_lists = [0.5, 4.5, 2.0, 7.7, 9.0, 15.2]
        self.asserteEqual(max_integer(float_lists), 15.2)

    def test_floats_and_ints(self):
        """ Test for floats and int of a list """
        float_int = [0.5, 4, 2.0, 7, 10, 9.0, 15.2]
        self.asserteEqual(max_integer(float_int), 10)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_array_at_beg(self):
        """Test for array that has max at the beginning."""
        arr_beg = [6, 5, 4, 3, 2]
        self.assertEqual(max_integer(arr_beg), 6)

    def test_array_at_mid(self):
        """Test for array that has max at the middle."""
        arr_mid = [4, 5, 7, 3, 2]
        self.assertEqual(max_integer(arr_mid), 8)

    def test_array_at_end(self):
        """Test for array that has max at the end."""
        arr_end = [6, 5, 4, 3, 10]
        self.assertEqual(max_integer(arr_end), 10)


if __name__ == '__main__':
    unittest.main()
