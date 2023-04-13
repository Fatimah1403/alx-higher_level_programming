#!/usr/bin/python3
"""Append a string at the end of a text file UTF8"""


def append_write(filename="", text=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write('text')
