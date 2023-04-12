#!/usr/bin/python3

"""inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """ The class of Rectangle which inherits the BaseGeometry class"""

    def __init__(self, width, height):
        """initialize a new rectangle """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
