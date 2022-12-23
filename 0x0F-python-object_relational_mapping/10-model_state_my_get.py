#!/usr/bin/python3
"""
 prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_a_state():
    """
    Querying db for list of State
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == searched_state
                                        ).order_by(State.id).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")


if __name__ == "__main__":
    get_a_state()
