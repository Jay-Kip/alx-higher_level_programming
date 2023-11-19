#!/usr/bin/python3
'''A secure script which takes in argument'''
import sys
import MySQLdb


if __name__ == "__main__":
    '''Establish a connection to the database'''
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    '''Create a cursor'''
    cursor = db.cursor()

    '''Excecute SQL commands'''
    search_word = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(search_word], ))

    '''Fetch all the rows retured by the query'''
    rows  = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
