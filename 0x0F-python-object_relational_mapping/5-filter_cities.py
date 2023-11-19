#!/usr/bin/python3
''' takes in the name of a state as an argument
and lists all cities of that state'''
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

    '''Excecute SQL statements
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN
                   states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4], ))'''

    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    '''Fetch all the rows returned by the query'''
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
