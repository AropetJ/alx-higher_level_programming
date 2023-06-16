#!/usr/bin/python3
# 1-search_replace.py
# by: Aropet_Joel

def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element by another in a new list."""
    nw_list = list(map(lambda x: replace if x == search else x, my_list))
    return (nw_list)
