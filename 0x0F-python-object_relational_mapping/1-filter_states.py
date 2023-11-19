#!/usr/bin/python3
"""  lists all states from the database"""
import sys
import MySQLdb


if __name__ == "__main__":
    '''Create a connection to the database'''
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    '''Create a Cursor'''
    cursor = db.cursor()
    '''Execute SQL statements'''
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id""")

    '''fetch all rows returned'''
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
