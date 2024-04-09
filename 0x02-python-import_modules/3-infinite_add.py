#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    count = 1
    total = 0
    while count < len(argv):
        total += int(argv[count])
        count += 1
    print(total)
