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
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1] + [tri[i] + tri[i + 1] \
                     for i in range(len(tri) - 1)] + [1]
        triangles.append(tmp)
    return triangles
