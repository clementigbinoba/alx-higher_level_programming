#!/usr/bin/python3
"""Construct a Rectangle class."""

class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle object with given width and height."""
        self.set_dimensions(width, height)

    def set_dimensions(self, width, height):
        """Sets the dimensions of the rectangle."""
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Dimensions must be integers.")
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative.")
        self.width = width
        self.height = height

    def get_area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle with width {self.width} and height {self.height}."
