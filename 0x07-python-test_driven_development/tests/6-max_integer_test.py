#!/usr/bin/python3
"""Module Includes a class containing
unittest methods for max_integer()
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    """ test cases for the max_integer()
    """
    def test_integers(self):
        """ tests that expected output is correct"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_floats(self):
        """ tests that expected output is correct"""
        result = max_integer([11.1, 23.86, 9.8, 4])
        self.assertEqual(result, 23.86)

    def test_negative_integers(self):
        """ tests that expected output is correct"""
        result = max_integer([-11, -23, -1, -4])
        self.assertEqual(result, -1)

    def test_zeros(self):
        """ tests that expected output is correct"""
        result = max_integer([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_same_integer(self):
        """ tests that expected output is correct"""
        result = max_integer([99, 99, 99, 99])
        self.assertEqual(result, 99)

    def test_empty(self):
        """ tests that expected output is correct"""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_list_comprehension(self):
        my_list = [1, 2, 3, 4]
        result = max_integer([pow(i, 2) for i in my_list])
        self.assertEqual(result, 16)

    def test_atleast_one_element(self):
        """ tests that expected output is correct"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_large_list(self):
        """ tests that expected output is correct"""
        result = max_integer([
            34, 23, 9, 40, 99, 1000, 2022, 50,
            333, 555, 777, 44, 91, 39, 28, 923,
            2011, 505, 322, 748, 888, 2, 5])
        self.assertEqual(result, 2022)

    def test_single_number(self):
        """ tests that expected output is correct"""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_string_in_list(self):
        """ test for element type"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'A', 3])

    def test_tuple_in_list(self):
        """ test of element type"""
        with self.assertRaises(TypeError):
            max_integer([1, (2, 3), 4])

    def test_hexa_numbers(self):
        """ test that expected output is correct"""
        result = max_integer([0xfffffe, 0xffffee, 0xfffffc, 0xffffea])
        self.assertEqual(result, 16777214)

    def test_bool_in_list(self):
        """ test that expected output is correct"""
        result = max_integer([1, 2, 3, True])
        self.assertEqual(result, 3)

    def test_all_letters(self):
        """tests that expected output is correct"""
        result = max_integer(['a', 'b', 'c', 'd'])
        self.assertEqual(result, 'd')
