#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them
   to a file"""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    items = (
        load_from_json_file("add_item.json")
        if os.path.isfile("add_item.json")
        else []
    )
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
