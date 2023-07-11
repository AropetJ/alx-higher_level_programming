#!/usr/bin/python3
"""Defines a class Student
"""


class Student:
    """initialise the class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a the attributes of the student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that returns the dictionary representation of Student
           If attrs is a list of strings, only attribute names contained in
           this list must be retrieved.
           Otherwise, all attributes must be retrieved

        Args:
            attrs (list): (Optional) The attributes to be represent.
        """
        if type(attrs) == list and \
                all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """A function that replaces all attributes of the Student instance

        Args:
            json (dict): The key/value pairs to be used to replace the
            attributes.
        """
        for k, v in json.items():
            self.__dict__[k] = v
