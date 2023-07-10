#!/usr/bin/python3
"""Defines a class Mylist"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
