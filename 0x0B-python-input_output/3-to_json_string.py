#!/usr/bin/python3
"""Module of returning JSON string """
import json


def to_json_string(my_obj):
    """ Returning the JSON representation of an object"""
    return json.dumps(my_obj)
