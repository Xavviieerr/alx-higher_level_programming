#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletable_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            deletable_keys.append(key)
    if not deletable_keys == []:
        for key in deletable_keys:
            del a_dictionary[key]
    return a_dictionary
