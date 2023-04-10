#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
