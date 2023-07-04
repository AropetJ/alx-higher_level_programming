#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>

    Args:
        first_name (str): A string containing the first name.
        last_name (str): A string containing the last name.
    Raises:
        TypeError: First_name must be a string or last_name must be a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
