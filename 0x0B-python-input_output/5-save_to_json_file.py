#!/usr/bin/python3
"""Defines a function that writes an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
       using a JSON representation

    Args:
        my_obj (object): The source object file
        filename (txt): The text filename
    """
    with open(filename, "w") as fWrite:
        json.dump(my_obj, fWrite)
