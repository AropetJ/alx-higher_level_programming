#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list
       and only integers.

    Args:
        my_list (list): The list who's elements are to be printed.
        x (int): Represents the number of elements to access in my_list.

    Returns:
        The real number of integers printed.
    """
    real_number = 0
    for i in range(0, x):
        try:
            i = "{:d}"
            print(i.format(my_list[i]), end="")
            real_number += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real_number)
