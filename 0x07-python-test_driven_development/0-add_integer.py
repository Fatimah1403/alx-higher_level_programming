#!/usr/bin/python3
"""
The module is about adding two integers

"""


def add_integer(a, b=98):
    """Return sum of two intergers or floats

    Args:
        a is the first argument
        b is the second argument

    Returns:
        sum of a and b

    Raises:
    TypeErrror: if the arguments are not int or float


    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a + b))
