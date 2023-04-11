#!/usr/bin/python3
"""
have inherits_of function
"""

def inherits_from(obj, a_class):
    """Returns True if `obj` is a subclass of `a_class`, otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
