#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list.

    Args:
        my_list (list): The list who's elements are to be printed.
        x (int): Represents the number of elements to print.

    Returns:
        The real number of elements printed.
    """
    real_number = 0
    for j in range(x):
        try:
            k = "{}"
            print(k.format(my_list[j]), end="")
            real_number += 1
        except IndexError:
            break
    print("")
    return (real_number)
