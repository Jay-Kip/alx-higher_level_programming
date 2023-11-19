#!/usr/bin/python3

""" Lists all states with name starting with {N}"""
import sys
import MySQLbd


if __name__ == "__main__":
    '''Establish a connection to the database'''
    db = MyQSLdb.connect(host="localhost",
                       user=sys.argv[1],
                       passwd=sys.argv[2],
                       db=sys.argv[3],
                       port=3306)

    '''Create cursor'''
    cursor = db.cursor()
    '''execute SQL query'''
    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE BINARY 'N%'
                   OREDER BY states.id""")

    '''Fetching all the rows returned by the query'''
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
