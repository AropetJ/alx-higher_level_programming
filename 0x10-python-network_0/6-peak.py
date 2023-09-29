#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): A list of unsorted integers
    Returns: The peak integer in the list of integers
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        middle = (left + right) // 2

        if list_of_integers[middle] >= list_of_integers[middle + 1]:
            right = middle
        else:
            left = middle + 1

    return list_of_integers[left]
