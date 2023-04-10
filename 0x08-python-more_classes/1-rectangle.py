#!/usr/bin/python3
"""Construct a Rectangle class."""


class Rectangle:
    """stands foa a rectangle."""

    def __init__(self, width=0, height=0):
        """Begin with a new set of Rectangle.
        Args:
            width (int):  rectangle width  .
            height (int):  height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of the rectangle set."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Rectangle height set."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
