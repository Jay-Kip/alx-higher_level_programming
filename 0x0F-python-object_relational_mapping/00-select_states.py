#!/usr/bin/python3
import MySQLdb

def list_states(username, password, database):
    '''Connect to MySQL server'''
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    '''Create a cursor'''
    cursor = db.cursor()

    '''Excecute the query to retrieve all states'''
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    '''Fetch all yhe rows returned by the querry'''
    rows = cursor.fetchall()

    '''Print the states'''
    for row in rows:
        print(row)

    '''Close the cursor'''
    cursor.close()
    db.close()
