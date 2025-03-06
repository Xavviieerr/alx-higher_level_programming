#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return(None)
    largest = float('-inf')
    the_key = None
    for key, value in a_dictionary.items():
        if value > largest:
            largest = value
            the_key = key
    return(the_key)
