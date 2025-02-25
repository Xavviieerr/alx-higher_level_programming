#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    len_arg = len(argv)
    if len_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            sum = add(a, b)
            print("{} {} {} = {}".format(a, argv[2], b, sum))
        elif  argv[2] == "-":
            minus = sub(a, b)
            print("{} {} {} = {}".format(a, argv[2], b, minus))
        elif argv[2] == "*":
            times = mul(a, b)
            print("{} {} {} = {}".format(a, argv[2], b, times))
        elif argv[2] == "/":
            divide = div(a, b)
            print("{} {} {} = {}".format(a, argv[2], b, divide))
