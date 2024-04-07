#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    endtext = 'and is less than 6 and not 0'
    print(f"Last digit of {num} is {-(-num % 10)} {endtext}")
elif num % 10 > 5:
    print(f"Last digit of {num} is {num % 10} and is greater than 5")
elif num % 10 == 0:
    print(f"Last digit of {num} is {num % 10} and is 0")
else:
    print(f"Last digit of {num} is {num % 10} and is less than 6 and not\
                              0")
