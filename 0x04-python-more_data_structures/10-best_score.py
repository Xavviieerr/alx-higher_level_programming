#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return(None)
    largest = 0
    the_key = ""
    for x in sorted(a_dictionary):
        if a_dictionary[x] > largest:
            largest = a_dictionary[x]
            the_key = x
    return(the_key)
