#!/usr/bin/python3
# 2-uniq_add.py
# by: Aropet_Joel

def uniq_add(my_list=[]):
    """A function that adds all unique
    integers in a list (only once for
    each integer).
    """
    uniq_list = set(my_list)
    i = 0

    for j in uniq_list:
        i += j

    return (i)
