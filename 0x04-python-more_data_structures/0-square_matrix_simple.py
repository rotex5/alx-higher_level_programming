#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    # row = len(matrix)
    column = len(matrix[0])
    temp = [[row[i]**2 for row in matrix] for i in range(column)]
    new_mat = [[row[i] for row in temp] for i in range(column)]
    return (new_mat)
