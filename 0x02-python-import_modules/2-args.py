#!/usr/bin/python3
import sys
list = sys.argv
len_list = len(list) - 1
if __name__ == '__main__':
    if len_list == 0:
        print("{} arguments.".format(len_list))
    if len_list >= 1:
        print("{} arguments :".format(len_list))
        for x in range(1, len_list + 1):
            print("{}: {}".format(x, list[x]))
