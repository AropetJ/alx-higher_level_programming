#!/usr/bin/python3
# 0-print_list_integer.py
# By: Aropet_Joel

def print_list_integer(my_list=[]):
    """A function that prints all integers of a list."""
    for i in range(len(my_list)):
        x = "{:d}"
        print(x.format(my_list[i]))
