#!/usr/bin/python3
""" The modules defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserting a line of text to a file"""
    txt = ""
    with open(filename) as k:
        for line in k:
            txt += line
            if search_strings in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
