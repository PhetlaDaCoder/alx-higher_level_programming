#!/usr/bin/python3
"""Defines a function that writes an Object to text file, using JSON
"""
import json


def from_json_string(my_str):
    """Module save_to_json_file
    accepts Python object and sends JSON to file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
