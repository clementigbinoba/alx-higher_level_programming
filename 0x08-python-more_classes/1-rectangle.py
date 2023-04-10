   #!/usr/bin/python3
"""
This program defines a Rectangle class.
"""

class Rectangle:
"""
This class represents a rectangle.
"""
def init(self, width=0, height=0):
"""                                                                                                                                                                     Args:
    - width (int): The width of the new rectangle.
    - height (int): The height of the new rectangle.
    """
    self.width = width
    self.height = height

@property
def width(self):
    """Returns the width of the rectangle."""
    return self.__width

@width.setter
def width(self, value):
    """Sets the width of the rectangle."""
    if not isinstance(value, int):
        raise TypeError("Width must be an integer.")
    if value < 0:
        raise ValueError("Width must be greater than or equal to 0.")
    self.__width = value

@property
def height(self):
    """Returns the height of the rectangle."""
    return self.__height

@height.setter
def height(self, value):
    """Sets the height of the rectangle."""
    if not isinstance(value, int):
        raise TypeError("Height must be an integer.")
    if value < 0:
        raise ValueError("Height must be greater than or equal to 0.")
    self.__height = value
