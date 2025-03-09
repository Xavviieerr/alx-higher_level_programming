#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for x in range(0, list_length):
            if isinstance(my_list_1[x], (float, int)) and isinstance(my_list_2[x], (float, int)):
                if my_list_2[x] ==0:
                    print("division by 0")
                    new_list.append(0)
                else:
                    new_list.append(my_list_1[x] / my_list_2[x])
            else:
                print("wrong type")
                new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        return new_list
