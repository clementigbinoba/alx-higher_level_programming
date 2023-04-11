#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    def __init__(self):
        list.__init__(self)
        
    def get_first(self):
        if len(self) > 0:
            return self[0]
        else:
            return None


