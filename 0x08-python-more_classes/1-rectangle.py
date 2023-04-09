#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""
        self._width = width
        self._height = height

    def __str__(self):
        """Method that returns the string representation of the rectangle"""
        return f"Rectangle(width={self._width}, height={self._height})"

    def area(self):
        """Method that calculates and returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Method that calculates and returns the perimeter of the rectangle"""
        return 2 * (self._width + self._height)

    @property
    def width(self):
        """Method that returns the value of the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Method that sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Method that returns the value of the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Method that sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
