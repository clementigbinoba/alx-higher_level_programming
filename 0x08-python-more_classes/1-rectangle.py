#!/usr/bin/python3
"""Construct a Rectangle class."""


class Rectangle:
    """Stand for a rectangle."""

    def __init__(self, width=0, height=0):
        """Starting point for the Rectangle.

        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representing rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        """Obtain width of rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """get width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Obtain height rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Obtain height rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
