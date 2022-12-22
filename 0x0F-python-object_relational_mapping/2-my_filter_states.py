#!/usr/bin/python3
"""A script that Lists state with a name
inputed by the user
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Querying db for data based on the state passed by user
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3],
                                    host='localhost',
                                    port=3306,
                                    charset='utf8')

    cursor = db_connection.cursor()
    query = "SELECT id, name FROM states WHERE BINARY name='{}' ORDER BY id ASC;"
    cursor.execute(query.format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_connection.close()
