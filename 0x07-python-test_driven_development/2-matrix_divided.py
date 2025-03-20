#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and rounds to 2 decimal places.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with the divided values.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If all rows in the matrix are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
