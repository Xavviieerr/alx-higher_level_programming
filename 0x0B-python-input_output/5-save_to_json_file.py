#!/usr/bin/python3
"""main file"""
import json

def save_to_json_file(my_obj, filename):
    """write to atext file using json"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
