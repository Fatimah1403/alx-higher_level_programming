#!/usr/bin/python3
""" A rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """ A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initilizing the attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # getters of all attributes
    @property
    def width(self):
        """ value of the width"""
        return self.__width

    @property
    def height(self):
        """ value of the height"""
        return self.__height

    def x(self):
        """ value of x"""
        return self.__x

    def y(self):
        """ value of y"""
        return self.__y

    # setters of all attributes
    @width.setter
    def width(self, val):
        """ setting the value for the width"""
        if (type(val) is not int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """ setting the value for the height"""
        if (type(val) is not int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """ setting the value for x"""
        if (type(val) is not int):
            raise TypeError("x must be an integer")
        if val <= 0:
            raise ValueError("x must be >= 0")
        self.x = val

    @y.setter
    def y(self, val):
        """ setting the value for y"""
        if (type(val) is not int):
            raise TypeError("y must be an integer")
        if val <= 0:
            raise ValueError("y must be >= 0")
        self.y = val

    def area(self):
        """ Area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Printing in the stdout the Rectangle instance with character # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
        for column in range(self.__width):
            print("#", end="")
            print()

    def __str__:
        """ string representation of class Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigning an argument to each attributes """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.width = arg
                elif ar == 2:
                    self.height = arg
                elif ar == 3:
                    self.x = arg
                elif ar == 4:
                    self.y = arg
            ar += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        new_dict = {"id": self.id, "width": self.__width,
                    "height": self.__height, "x": self.__x,
                    "y": self.__y}

        return new_dict
