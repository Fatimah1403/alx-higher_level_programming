#!/usr/bin/python3
""" Module that convert JSON string to object"""
import json


def from_json_string(my_str):
    """ Returning an object represented by a JSON string"""
    return json.loads(my_str)
