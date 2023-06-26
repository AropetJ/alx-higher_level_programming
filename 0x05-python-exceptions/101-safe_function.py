#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """A function that executes a function safely.

    Args:
        fct: A pointer to a function.
        args: Arguments to the function pointed to.

    Returns:
        the result of the function,.
        Otherwise, returns None if something happens
        during the function and prints in stderr the
        error precede by Exception:
    """
    try:
        result = fct(*args)
        return (result)
    except (TypeError, ValueError, ZeroDivisionError, IndexError):
        i = "Exception: {}"
        print(i.format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
