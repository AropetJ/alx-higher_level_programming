#!/usr/bin/python3
# 101-square_matrix_map.py
# by: Aropet_Joel

def square_matrix_map(matrix=[]):
    """A function that computes the square value of all integers of a matrix using map"""
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
