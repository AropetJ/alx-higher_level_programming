#!/usr/bin/python3
# 0-square_matrix_simple.py
# by: Aropet_Joel

def square_matrix_simple(matrix=[]):
    """A function that computes the square value of
    all integers of a matrix.
    """
    nw_mtrx = matrix.copy()

    for j in range(len(matrix)):
        nw_mtrx[j] = list(map(lambda x: x**2, matrix[j]))

    return (nw_mtrx)
