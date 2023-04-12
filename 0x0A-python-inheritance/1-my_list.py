#!/usr/bin/python3

""" Public instance of a method that prints the list"""


def print_sorted(self):
    """ print a sorted lists """
    if issubclass(MyList, list):
        print(sorted(self))
