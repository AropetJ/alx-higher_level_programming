#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# by: Aropet_Joel

def print_sorted_dictionary(a_dictionary):
        """A function that prints a dictionary by ordered keys"""
        list_ordered = list(a_dictionary.keys())
        list_ordered.sort()
        for j in list_ordered:
            x = "{}: {}"
            print(x.format(j, a_dictionary.get(j)))
