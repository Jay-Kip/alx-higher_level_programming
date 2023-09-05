#!/usr/bin/python3

def matrix_divided(matrix, div):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []


    for i in range(rows):
        new_row = []
        for j in range(cols):
            value = matrix[i][j] / div
            rounded_value = round(value, 2)
            new_row.append(rounded_value)
        new_matrix.append(new_row)

    return new_matrix