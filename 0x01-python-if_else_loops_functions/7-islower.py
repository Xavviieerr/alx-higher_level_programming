#!/usr/bin/python3
def islower(c):
    asc_value = ord(c)
    if asc_value >= 97 and asc_value <= 122:
        return True
    else:
        return False
