#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("".format())
    for row in matrix:
        if len(row) == 3:
            print("{:d} {:d} {:d}".format(row[0], row[1], row[2]))
        elif len(row) == 2:
            print("{:d} {:d}".format(row[0], row[1]))
        elif len(row) == 1:
            print("{:d}".format(row[0]))
