#!/usr/bin/python3
"""Defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
       and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    Returns:
        The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as fWrite:
        return fWrite.write(text)
