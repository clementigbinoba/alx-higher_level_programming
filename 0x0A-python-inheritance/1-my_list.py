#!/usr/bin/python3
"""
contains the MyList class
"""

class MyList(list):
    def __init__(self, *args, **kwargs):
        super(MyList, self).__init__(*args, **kwargs)
        
    def get_first(self):
        return self[0] if len(self) > 0 else None




