#!/usr/bin/python3
"""A script that Lists state with a name
inputed by the user
"""
import sys
import MySQLdb


def filter_state():
    """
    Querying db for data based on the state passed by user
    """
    try:
        db_connection = MySQLdb.connect(user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3],
                                        host='localhost',
                                        port=3306,
                                        charset='utf8')
    except Exception:
        print("Can't connect to database")
        return 0

    cursor = db_connection.cursor()
    query = "SELECT id, name FROM states WHERE name='{}' ORDER BY id ASC;"
    cursor.execute(query.format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    filter_state()
