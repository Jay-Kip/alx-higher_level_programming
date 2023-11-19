#!/usr/bin/python3
'''Takes an argument Displays all values in the states table'''
import sys
import MySQLdb


if __name__ == "__main__":
    '''Establich a connection to the database'''
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    '''Create a cursor'''
    cursor = db.cursor()

    '''Excecute SQL commands'''
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))

    '''Fetch all the rows returned by the query'''
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
