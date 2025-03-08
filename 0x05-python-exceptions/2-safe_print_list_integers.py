#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        new_list = list(map(lambda item: item, my_list))
        length = 0
        count = 0
        for w in new_list:
            length += 1
        if x <= length:
            for y in range(0, x):
                if isinstance(new_list[y], int):
                    count += 1
                    print("{:d}".format(new_list[y]), end="")
            print()
        else:
            raise IndexError("Index out of range")
        return count
    except IndexError as e:
        print(f"Error: {e}")

