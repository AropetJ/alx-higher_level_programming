#!/usr/bin/python3
"""Defines a function that returns a python data structure"""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
       represented by a JSON string

    Args:
        my_str (str): The string whose representation is to returned

    Returns:
        object: Python data structure
    """
    return json.loads(my_str)
