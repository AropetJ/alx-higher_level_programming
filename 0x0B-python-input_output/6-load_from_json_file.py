#!/usr/bin/python3
"""Defines a function that creates an object"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a
       “JSON file”

    Args:
        filename (json): The json file to create an object

    Returns:
        object: python data structure
    """
    with open(filename) as fCreate:
        return json.load(fCreate)
