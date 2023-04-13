#!/usr/bin/python3
""" Reading from a text file using (UTF8)"""


def read_file(filename=""):
    """ Print the content of the utf-8 file """
    with open('filename', encoding='utf-8') as f:
        print(f.read(), end="")
