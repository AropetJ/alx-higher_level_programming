#!/usr/bin/python3
# 6-print_matrix_integer.py
# by: Aropet_Joel

def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers."""
    for i in matrix:
        for j in i:
            x = "{:d}"
            print(x.format(j), end=" "if j != i[-1] else"")
        print()
