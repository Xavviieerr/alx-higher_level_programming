#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        value = ord(char)
        if 97 <= value <= 122:
            value -= 32
        result += chr(value)
    print("{}".format(result))
