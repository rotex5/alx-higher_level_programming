#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def from_city():
    """
    Start link class to table in database
    to perform list query
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).join(City).order_by(City.id).all()

    for state in instance:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == "__main__":
    from_city()
