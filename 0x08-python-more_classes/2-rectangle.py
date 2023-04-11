#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""  


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    
    def get_width(self):
        return self._width
    
    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be non-negative.")
        self._width = value
    
    def get_height(self):
        return self._height
    
    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be non-negative.")
        self._height = value
    
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
