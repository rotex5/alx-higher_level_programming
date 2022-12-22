#!/usr/bin/python3
"""A script that Lists all states with a name starting
with N from the a db hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Querying db for states that start with 'N'
    """
    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3],
                                    host='localhost',
                                    port=3306)

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                   ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db_connection.close()
