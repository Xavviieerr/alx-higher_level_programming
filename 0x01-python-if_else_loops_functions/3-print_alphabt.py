#!/usr/bin/python3
letter = ""
for x in range(97, 123):
    if x != 113:
        if x != 101:
             letter += "{}".format(chr(x))
print(letter, end="")
