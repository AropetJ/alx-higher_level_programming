#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """ A function that adds 2 integers a and b.

    Args:
        a(int): The first int argument, can also be a float.
        b(98): The second integer argument
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
