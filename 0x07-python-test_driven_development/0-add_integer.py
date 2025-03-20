#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
The function ensures that both arguments are integers or floats.
If necessary, it converts float inputs to integers before performing addition.
"""
def add_integer(a, b=98):
    """
        Adds two numbers and returns the result.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
