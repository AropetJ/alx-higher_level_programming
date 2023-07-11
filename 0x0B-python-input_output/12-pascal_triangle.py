#!/usr/bin/python3
"""Defines a function that prints pascals triangle"""


def pascal_triangle(n):
    """Defines a function that prints pascals triangle.

    Args:
        n (int): The integer whose pascal's triangle is to
                 be found.

    Returns:
        triangles: returns a list of lists of integers
                   representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    for _ in range(1, n):
        prev_row = triangles[-1]
        curr_row = [1]

        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i + 1])

        curr_row.append(1)
        triangles.append(curr_row)

    return triangles
