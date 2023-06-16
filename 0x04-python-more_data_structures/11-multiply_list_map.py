#!/usr/bin/python3
# 11-multiply_list_map.py
# by: Aropet_Joel

def multiply_list_map(my_list=[], number=0):
    """A function that returns a list with all values multiplied by a number without using any loops"""
    return (list(map((lambda i: i * number), my_list)))
