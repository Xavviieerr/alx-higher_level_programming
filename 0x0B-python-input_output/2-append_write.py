#!/usr/bin/python3
"""main file"""
def append_write(filename="", text=""):
    """append write function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
