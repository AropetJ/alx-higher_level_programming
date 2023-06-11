#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# by: Aropet_Joel

def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list, in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for j in my_list:
            x = "{:d}"
            print(x.format(j))
