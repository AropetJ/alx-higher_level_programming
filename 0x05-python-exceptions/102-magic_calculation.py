#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b):
    """A function def magic_calculation(a, b): that
    does exactly the same as the following Python bytecode.

    Args:
        a: A pointer to a function.
        b: Arguments to the function pointed to.

    Returns:
        the result of the function,.
    """
    result = 0
    try:
        if 1 > a:
            raise Exception('Too far')
        else:
            result += a ** b / 1

        if 2 > a:
            raise Exception('Too far')
        else:
            result += a ** b / 2

    except Exception as e:
        result = b + a
    return (result)
