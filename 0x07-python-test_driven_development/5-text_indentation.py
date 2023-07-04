#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a  a text with 2 new lines after each of these
   characters: ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (string): A string to print and test our fucntion.
    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = 0
    result = len(text) - len(text.lstrip())

    while result < len(text):
        print(text[result], end="")
        if text[result] == "\n" or text[result] in ".?:":
            if text[result] in ".?:":
                print("\n")
            result += 1
            while result < len(text) and text[result] == ' ':
                result += 1
            continue
        result += 1
