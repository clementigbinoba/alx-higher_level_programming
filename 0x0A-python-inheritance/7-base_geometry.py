#!/usr/bin/python3
"""
include BaseGeometry class 
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

            
            class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def __init__(self):
        self._area = None

    def area(self):
        """Calculates and returns the area"""
        raise NotImplementedError("area() method is not implemented")

    def set_area(self, area):
        """Sets the area"""
        if not isinstance(area, (int, float)):
            raise TypeError("Area must be a number")
        if area < 0:
            raise ValueError("Area cannot be negative")
        self._area = area

    def get_area(self):
        """Returns the area"""
        return self._area

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
