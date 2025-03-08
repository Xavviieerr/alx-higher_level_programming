#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix =list(map(lambda x: x[:], matrix))
    return list(map(lambda row: list(map(lambda col: col ** 2, row)), new_matrix))
