#!/usr/bin/python3
num = 0
for x in range(0, 9):
    num += 1
    for y in range(num, 10):
        if x == 8 and y == 9:
            print("{}".format(89))
        else:
            print("{}{}, ".format(x, y), end="")
