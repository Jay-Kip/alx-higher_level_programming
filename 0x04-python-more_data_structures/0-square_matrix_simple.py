#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for i in range(0, len(new)):
        new[i] = list(map(lambda m: m ** 2, matrix[i]))
    return (new)
