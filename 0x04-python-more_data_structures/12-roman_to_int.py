#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0  # Handle invalid input
    
    my_dictionary = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
        "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }

    accumulator = 0
    x = 0
    length = len(roman_string)

    while x < length:
        if x + 1 < length and roman_string[x:x+2] in my_dictionary:
            accumulator += my_dictionary[roman_string[x:x+2]]
            x += 2
        else:
            accumulator += my_dictionary[roman_string[x]]
            x += 1
    return (accumulator)
