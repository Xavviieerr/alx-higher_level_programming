#!/usr/bin/python3
for x in range(0, 9):
    for y in range(1, 10):
        if x == 8 and y == 9:
            print("{}".format(89))
        else:
            print("{}{}, ".format(x, y), end="")
