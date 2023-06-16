#!/usr/bin/pyhton3
# 5-number_keys.py
# by: Aropet_Joel

def number_keys(a_dictionary):
    """A function that returns the number of keys in a dictionary."""
    i = 0
    list_the_keys = list(a_dictionary.keys())

    for j in list_the_keys:
        i += 1

    return (i)
