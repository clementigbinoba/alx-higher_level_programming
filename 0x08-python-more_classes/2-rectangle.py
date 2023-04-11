#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""  


class Rectangle:
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)
        
    def get_width(self):
        return self.__width
        
    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        
    def get_height(self):
        return self.__height
        
    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        
    def area(self):
        return self.get_width() * self.get_height()
    
    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())
