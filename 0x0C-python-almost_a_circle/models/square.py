#!/usr/bin/python3
"""A square class that inherits from Rectangle class """

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Initilizes the attributes """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of class square"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    """ getting the getter of size attribute """
    def size(self):
        """ get the value of size"""
        return self.__width

    @size.setter
    def size(self):
        """ get the value of the size """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val
        self.__height = val

    def update(self, *args, **kwargs):
        """ Update attribute """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type([0]) != int and args[0] os not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of class square"""
        new_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return new_dict
