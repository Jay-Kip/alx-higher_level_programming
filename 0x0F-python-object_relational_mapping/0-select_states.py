#!/usr/bin/python3
'''Lists all states'''

import sys
import MySQLdb


if __name__ == "__main__":
    '''Establishing a connection to the database'''
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    '''creating  a cursor'''
    cursor = db.cursor()
    '''Executes an SQL query'''
    cursor.execute("SELECT * FROM states")

    '''fetches all the rows returned by the query'''
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
