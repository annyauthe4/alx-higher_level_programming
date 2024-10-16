#!/usr/bin/python3
"""This module includes a script that adds all arguments
to a Python list, and then save them to a file.
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
# Add all command-line args
items.extend(sys.argv[1:])

save_to_json_file(items, filename)
