#!/usr/bin/python3
"""
MyList class function
"""


class MyList(list):
    """a subclass of list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
