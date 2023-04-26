#!/usr/bin/python3
"""
Accommodate the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A description of a square"""
    def __init__(self, size):
        """image of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"remits the area of the square"""
        return self.__size ** 2
