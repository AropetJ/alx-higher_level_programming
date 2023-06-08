#!/usr/bin/python3
if __name__ == "__main__":
    """ a program that imports functions from a
    file, does some Maths, and prints the result.
    """
    from calculator_1 import sub, mul, div, add

    Args:
        a = 10
        b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
