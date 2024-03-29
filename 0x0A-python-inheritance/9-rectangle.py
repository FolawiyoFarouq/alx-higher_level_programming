#!/usr/bin/python3
"""
Accommodtae the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with common case procedures area and integer_validator"""
    def area(self):
        """lifts an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """confirm that value is an integer larger than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A description of a rectangle"""
    def __init__(self, width, height):
        """image of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """remits the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string description of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
