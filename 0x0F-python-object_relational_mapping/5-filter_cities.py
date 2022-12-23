#!/usr/bin/python3
"""a script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filter_state():
    """
    Querying db for data based on the state passed by user
    Implementing SQL Injection failsafe
    """
    try:
        searched_name = sys.argv[4]
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
    query = 'SELECT c.name'
    query += ' FROM cities c, states s'
    query += ' WHERE c.state_id = s.id AND s.name=%s'
    query += ' ORDER BY c.id ASC'
    cursor.execute(query, (searched_name,))
    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    filter_state()
