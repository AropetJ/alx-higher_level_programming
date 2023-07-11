#!/usr/bin/python3
"""Defines a function that appends a string"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of
       a text file (UTF8) and returns the number of characters added:

    Args:
        filename (str): The file to append to.
        text (str): The string to be appended to the file.
    Returns: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as fAppend:
        return fAppend.write(text)
