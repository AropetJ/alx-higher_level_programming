#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """A function that prints a square with the character #.

    Args:
        size (int): The size length of the square.
    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
