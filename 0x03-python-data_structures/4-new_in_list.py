#!/usr/bin/python3
# 4-new_in_list.py
# by: Aropet_Joel

def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list at a specific
    position without modifying the original list (like in C).
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    duplicate = [x for x in my_list]
    duplicate[idx] = element
    return duplicate
