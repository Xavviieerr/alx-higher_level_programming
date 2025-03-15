#!/usr/bin/python3
"""main module"""
class Square:
    """initializing"""
    def __init__(self,  size=0):
        """assighnment."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise  ValueError("size must be >= 0")
        self.__size = size


    """method that returns square area"""
    def area(self):
        """public instance method returns"""
        return (self.__size * self.__size)
