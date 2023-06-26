#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """A function that prints an integer with "{:d}".format().

    Args:
        value (int, string, etc): An integer to be printed in
        the specified format.

    Returns:
        True if value has been correctly printed (it means the value is an integer).
        Otherwise, returns false.
    """
    try:
        i = "{:d}"
        print(i.format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
