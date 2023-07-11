#!/usr/bin/python3
"""Defines a function script that adds all arguments to a python list"""


def class_to_json(obj):
    """A function that returns the dictionary description with simple data
       structure (list, dictionary, string, integer and boolean) for JSON
       serialization of an object

    Args:
        obj (list): A list containing arguments to be added

    Returns:
        dict: the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        serialization of an object
    """
    return obj.__dict__
