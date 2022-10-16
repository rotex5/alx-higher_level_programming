#!/usr/bin/python3
"""
This module includes a function that
divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix
    """
    l = len(matrix)
    for i in range(l):
        if matrix[i] == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    i = 0
    while i < (l-1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")
        i+=1
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number of integer/floats")

    new_mat = [[round((j/div), 2) for j in matrix[i]] for i in range(l)]
    return new_mat

