#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    def get_first(self):
        return self[0] if len(self) > 0 else None



