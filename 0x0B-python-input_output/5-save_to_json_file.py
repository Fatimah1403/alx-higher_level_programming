#!/usr/bin/python3
"""Module thant returns JSON string """
from json import dumps


def save_to_json_file(my_obj, filename):
    """ Returning the JSON representation of an object """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(dumps(my_obj))
