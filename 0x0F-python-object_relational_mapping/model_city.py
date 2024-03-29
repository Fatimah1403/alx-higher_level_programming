#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py
    that contains the class definition of a City
"""

import sqlalchemy
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ A city class that inherits from the baseclass
     Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to

    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """Object Representation"""
        return "<Cities(name =' %s')>" % (self.name)
