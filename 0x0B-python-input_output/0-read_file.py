#!/usr/bin/python3
"""main file"""
def read_file(filename=""):
    """reads afile"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
