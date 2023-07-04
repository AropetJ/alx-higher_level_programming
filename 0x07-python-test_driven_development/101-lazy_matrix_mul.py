#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ A function that multiplies 2 matrices by using the module NumPy

    Args:
        m_a (matrix): The first matrix.
        m_b (matrix): The second matrix.
    """

    return (np.matmul(m_a, m_b))
