#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
    """A function that prints an integer..

    Args:
        value (int): The integer to be printed.

    Returns:
        True if value has been correctly printed
        (it means the value is an integer)
        Otherwise, returns False and prints in
        stderr the error precede by Exception:
    """
    try:
        i = "{:d}"
        print(i.format(value))
        return (True)
    except (TypeError, ValueError):
        j = "Exception: {}"
        print(j.format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
