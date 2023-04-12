#!/usr/bin/python3
"""
hold the class BaseGeometry and class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        """calculates the area of the rectangle"""
        return self.width * self.height

    def __str__(self):
        """returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.width, self.height)
