#!/usr/bin/python3
"""A function that reads a text file (UTF8)
   and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file(UTF-8) and prints it to stdout

    Args:
        filename (str): The text file to be read from.
    """
    with open(filename, encoding="utf-8") as fPrint:
        print(fPrint.read(), end="")
