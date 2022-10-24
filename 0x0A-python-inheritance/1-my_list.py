#!/usr/bin/python3
""" Module includes a function that
inherits from list base class
"""


class MyList(list):
    """Inherites from list"""

    def print_sorted(self):
        """ prints sorted list in ascending order"""
        my_list = self.copy()
        my_list.sort()
        print(my_list)
