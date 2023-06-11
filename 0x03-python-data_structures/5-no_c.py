#!/usr/bin/python3
# 5-no_c.py
# by: Aropet_Joel

def no_c(my_string):
    """A function that removes all characters c and C from a string."""
    dupli = [i for i in my_string if i != 'c' and i != 'C']
    return "".join(dupli)
