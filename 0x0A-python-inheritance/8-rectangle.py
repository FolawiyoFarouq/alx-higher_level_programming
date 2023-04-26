#!/usr/bin/python3
"""Component 8-rectangle.
Generate a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Descrcibe a rectangle.
    """

    def __init__(self, width, height):
        """Computes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
