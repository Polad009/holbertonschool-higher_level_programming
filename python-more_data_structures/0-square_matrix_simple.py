#!/usr/bin/python3
"""Square matrix simple module"""


def square_matrix_simple(matrix=[]):
    """Returns new matrix with each value squared"""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
