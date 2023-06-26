#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """A function that divides 2 integers and prints the result."""

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        i = "Inside result: {}"
        print(i.format(div))
    return (div)
