#!/usr/bin/python3
"""This module defines a class Student"""


class Student:

    """Represent a student class."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve a dictionary representation of a student class """
        return self.__dict__
