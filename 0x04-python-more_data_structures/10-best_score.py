#!/usr/bin/python3
# 10-best_score.py
# by: Aropet_Joel

def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value"""
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
