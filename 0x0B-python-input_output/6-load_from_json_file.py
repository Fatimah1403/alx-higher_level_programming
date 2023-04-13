#!/usr/bin/python3
from json import loads
""" The module defines a JSON file-reading function"""


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
