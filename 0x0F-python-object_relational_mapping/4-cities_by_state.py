#!/usr/bin/python3
"""A script that  lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filter_cities():
    """
    Queryiing db for list of cicties.
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
    query = """SELECT c.id, c.name, s.name
                FROM cities c LEFT JOIN states s
                ON c.state_id = s.id
                ORDER BY c.id ASC"""
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    filter_cities()
