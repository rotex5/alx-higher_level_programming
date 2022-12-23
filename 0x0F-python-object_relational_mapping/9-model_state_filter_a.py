#!/usr/bin/python3
"""
Lists all State objects objects that contain
the letter `a` from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_states_with_a():
    """
    Querying db for list of States
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")
                                         ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_states_with_a()
