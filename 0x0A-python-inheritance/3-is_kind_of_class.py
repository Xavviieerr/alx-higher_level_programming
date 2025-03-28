#!/usr/bin/python3
"""main file"""
def is_kind_of_class(obj, a_class):
    """
    using is instance this time if the object is
    an instance of, or if the object is an 
    instance of a class that inherited from
    """
    return isinstance(obj, a_class)
