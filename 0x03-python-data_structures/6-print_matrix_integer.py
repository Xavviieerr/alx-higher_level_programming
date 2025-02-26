#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for row in matrix:
        if len(row) == 3:
            print("{} {} {}".format(row[0], row[1], row[2]))
        elif len(row) == 2:
            print("{} {}".format(row[0], row[1]))
        elif len(row) == 1:
            print("{}".format(row[0]))
