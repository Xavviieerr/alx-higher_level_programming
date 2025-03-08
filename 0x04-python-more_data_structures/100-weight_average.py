#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return(0)
    upper = 0
    lower = 0
    for x in my_list:
        upper += x[0] * x[1]
        lower += x[1]
    average = upper / lower
    return(average)
