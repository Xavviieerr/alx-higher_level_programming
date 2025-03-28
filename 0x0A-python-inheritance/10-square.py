#!usrbinpython3
"""main file"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """main class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
