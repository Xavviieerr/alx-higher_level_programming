#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = list(map(lambda item: item, my_list))
    length = 0
    count = 0
    for w in new_list:
        length += 1
    if x <= length:
        for y in range(0, x):
            try:
                if isinstance(new_list[y], int):
                    count += 1
                    print("{:d}".format(new_list[y]), end="")
            except IndexError:
                print()
                raise IndexError("Index out of range")
        print()
        return count
