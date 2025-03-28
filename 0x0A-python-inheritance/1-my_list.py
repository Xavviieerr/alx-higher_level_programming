#!/usr/bin/python3
"""Module that defines MyList class"""

class MyList(list):
    """Custom list class that inherits from built-in list"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
