#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def cities_in_state():
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
    Session = sessionmaker(bind=engine)
    session = Session()

    state_n_city = session.query(State, City).filter(
                            State.id == City.state_id).all()
    if state_n_city:
        for state, city in state_n_city:
            print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    cities_in_state()
