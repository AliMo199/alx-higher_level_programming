#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    word function computes square
    value of all integers of  matrix.
    """
    new_matrix = []
    for column in matrix:
        result = list(map(lambda x: x**2, column))
        new_matrix.append(result)
    return new_matrix
