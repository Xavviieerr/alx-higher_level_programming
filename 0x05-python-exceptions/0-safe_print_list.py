#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = list(map(lambda x: x, my_list))
        length = 0
        
        for element in new_list:
            length += 1
            
        if x > length:
            x = length
        
        for i in range(0, x):
            print(new_list[i], end="")
        print()
    except:
        print("error")
    return(x)
