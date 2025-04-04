#!/usr/bin/python3
"""main file"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """main class"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """claculates"""
        return self.__size * self.__size

    def __str__(self):
        """returns string"""
        return f"[Rectangle] {self.__size}/{self.__size}"
