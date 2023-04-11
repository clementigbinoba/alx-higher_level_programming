#!/usr/bin/python3
"""
has class function
"""

def is_kind_of_class(obj, a_class):
    """True if obj is inherited from a_class, else False"""
    return type(obj) is a_class or issubclass(type(obj), a_class)
