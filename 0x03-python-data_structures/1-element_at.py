#!/usr/bin/python3
# 1-element_at.py
# by: Aropet_Joel

def element_at(my_list, idx):
    """A function that retrieves an element from a list like in C."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
