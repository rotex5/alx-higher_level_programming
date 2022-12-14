#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def delete_states():
    """
    Start link class to table in database
    to perform delete query
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%")).all()
    if states:
        for state in states:
            session.delete(state)
    session.commit()


if __name__ == "__main__":
    delete_states()
