#!/usr/bin/python3
"""main file"""
def inherits_from(obj, a_class):
    """inherits from a sub class"""
    return isinstance(obj, a_class) and type(obj) != a_class
