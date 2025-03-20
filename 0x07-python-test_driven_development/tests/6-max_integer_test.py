#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with a sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([4, 2, 8, 1]), 8)

    def test_negative_numbers(self):
        """Test with a list containing only negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 0, 20, -3]), 20)

    def test_single_element(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_same_elements(self):
        """Test with a list where all elements are the same"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_one_negative_number(self):
        """Test with a list containing only one negative number"""
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_large_numbers(self):
        """Test with a list containing large numbers"""
        self.assertEqual(max_integer([1000000, 5000000, 9000000, 10000000]), 10000000)

if __name__ == '__main__':
    unittest.main()

