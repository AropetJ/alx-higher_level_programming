#!/usr/bin/python3
"""Defines a function that returns a JSON string
   representation
"""
import json


def to_json_string(my_obj):
    """"A function that returns the JSON representation
        of an object (string

    Args:
        my_obj (str): The string object

    Returns:
        json: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
