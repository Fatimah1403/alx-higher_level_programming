#!/usr/bin/python3
"""
A function that prints both first and last name

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the names
    Args:
        first_name (str): The first name of anything.
        last_name (str): The last name of anything.
    Raises:
        TypeError: If `first_name` and `last_name` aren't strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
