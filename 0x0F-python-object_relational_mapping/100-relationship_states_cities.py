#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""

import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def city_relationship():
    """
    Start link class to table in database
    to perform create query
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name='San Francisco', state='California')
    new_state = State(name='California')

    session.add(new_city)
    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    city_relationship()
