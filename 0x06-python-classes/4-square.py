#!/usr/bin/python3
"""main module"""
class  Square:
    """class square"""

    def __init__(self, size=0):
        """instantiates the size value"""
        self.size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the sizr"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the squared value"""
        return self.__size ** 2
