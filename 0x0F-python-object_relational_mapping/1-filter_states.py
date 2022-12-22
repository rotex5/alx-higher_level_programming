#!/usr/bin/python3
"""A script that Lists all states with a name starting
with N from the a db hbtn_0e_0_usa
"""
import sys
import MySQLdb


def filter_state():
    """
    Querying db for states that start with 'N'
    """
    try:
        db_connection = MySQLdb.connect(user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3],
                                        host='localhost',
                                        port=3306)
    except Exception:
        print("Can't connect to database")
        return 0

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                   ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == "__main__":
    filter_state()
