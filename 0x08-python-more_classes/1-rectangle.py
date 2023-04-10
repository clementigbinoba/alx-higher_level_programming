#!/usr/bin/python3

"""
This code defines a class Rectangle that can be used to create rectangle objects with specified width and height.
"""
class Rectangle:
"""
Empty class Rectangle that defines a rectangle.
"""
def __init__(self, width=0, height=0):
    """ 
    Initializes a new instance of the Rectangle class with optional width and height.
    
    Args:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
    """
    self.width = width
    self.height = height

@property
def width(self):
    """ 
    Getter method for the width property of the rectangle.
    
    Returns:
        int: The width of the rectangle.
    """
    return self.__width

@property
def height(self):
    """ 
    Getter method for the height property of the rectangle.
    
    Returns:
        int: The height of the rectangle.
    """
    return self.__height

@width.setter
def width(self, value):
    """ 
    Setter method for the width property of the rectangle.
    
    Args:
        value (int): The value to set the width of the rectangle to.
    
    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is negative.
    """
    if type(value) is not int:
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@height.setter
def height(self, value):
    """ 
    Setter method for the height property of the rectangle.
    
    Args:
        value (int): The value to set the height of the rectangle to.
    
    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is negative.
    """
    if type(value) is not int:
        raise TypeError("height must be an integer")
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

