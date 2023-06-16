#!/usr/bin/python3
# 9-multiply_by_2.py
# by: Aropet_Joel

def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary
    with all values multiplied by 2
    """
    new_dict = a_dictionary.copy()
    list_the_keys = list(new_dict.keys())

    for j in list_the_keys:
        new_dict[j] *= 2

    return (new_dict)
