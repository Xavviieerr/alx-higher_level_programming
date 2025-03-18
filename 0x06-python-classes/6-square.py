#!/usr/bin/python3
"""main module"""
class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with an optional size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints a square shaped #"""
        if self.__size == 0:
            print("")
        
        #print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
