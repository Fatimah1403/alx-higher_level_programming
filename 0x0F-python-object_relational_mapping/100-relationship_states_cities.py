#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.creat_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state_cal = State(name='California')
    new_city_san = City(name='San Francisco')
    new_state_cal.cities.append(new_city_san)

    session.add(new_state_cal)
    session.commit()

    session.close()
