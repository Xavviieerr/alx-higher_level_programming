#!/usr/bin/python3
"""
This module contains the function 'text_indentation'
which prints a text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    skip_space = False

    for char in text:
        new_text += char
        if char in ".:?":
            new_text += "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            skip_space = False

    print(new_text.strip())  # Ensure no extra spaces at the start or end

