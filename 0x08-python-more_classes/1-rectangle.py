#!/usr/bin/python3

"""
Module: rectangle.py
Description: Defines the Rectangle class.
"""

class Rectangle:
"""
Represents a rectangle with a width and height.
"""

def __init__(self, width=0, height=0):
    """
    Initializes a new instance of the Rectangle class.

    Args:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.
    """
    self._width = width
    self._height = height

def __str__(self):
    """
    Returns a string representation of the rectangle.

    Returns:
        A string representation of the rectangle.
    """
    return f"Rectangle(width={self._width}, height={self._height})"

def area(self):
    """
    Calculates and returns the area of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return self._width * self._height

def perimeter(self):
    """
    Calculates and returns the perimeter of the rectangle.

    Returns:
        The perimeter of the rectangle.
    """
    return 2 * (self._width + self._height)

@property
def width(self):
    """
    Gets the width of the rectangle.

    Returns:
        The width of the rectangle.
    """
    return self._width

@width.setter
def width(self, value):
    """
    Sets the width of the rectangle.

    Args:
        value (int): The new value for the width.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value

@property
def height(self):
    """
    Gets the height of the rectangle.

    Returns:
        The height of the rectangle.
    """
    return self._height

@height.setter
def height(self, value):
    """
    Sets the height of the rectangle.

    Args:
        value (int): The new value for the height.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value

