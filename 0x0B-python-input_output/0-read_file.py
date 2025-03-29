#!/usr/bin/python3
"""Function to read a text file and print its content"""

def read_file(filename=""):
    """Reads a UTF-8 encoded file and prints its contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
