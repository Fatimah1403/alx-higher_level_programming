#!/usr/bin/python3
""" The module defines a JSON file-reading function"""
from json import loads


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file """
    with open(filename, encoding="utf-8") as f:
        return loads(f.read())
