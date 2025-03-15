#!/usr/bin/python3
"""main class module."""
class Square:
    """this class adds condition to the size attribute."""

    def __init__(self, size=0):
        """condition for the size set below."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
