#!/usr/bin/python3
"""  lists all cities from the database"""
import sys
import MySQLdb


if __name__ == "__main__":
    '''Create a connection to the database'''
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    '''Create a Cursor'''
    cursor = db.cursor()

    '''Excecute SQL statements'''
    cursor.execute("""SELECT cities.id, cities.name , states.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id""")

    '''Fetch all rows returned by the query'''
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
