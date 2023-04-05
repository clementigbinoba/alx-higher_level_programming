#!/usr/bin/env python3

"""
This module defines a class that restricts the creation of dynamically added attributes.
"""

class LockedClass:
"""
A class that restricts the creation of dynamically added attributes by using __slots__.
"""

__slots__ = ['name']

def __init__(self):
"""
Initializes a new instance of the LockedClass.
"""
pass
