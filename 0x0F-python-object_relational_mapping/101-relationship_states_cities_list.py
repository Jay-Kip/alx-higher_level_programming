#!/usr/bin/python3
'''script that lists all State objects, and corresponding
City objects, contained in the database'''
from relationship_city import City
from relationship_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    '''Create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).order_by(State.id):
        print(i.id, i.name, sep=": ")
        for c in i.cities:
            print("    ", end="")
            print(c.id, c.name, sep=": ")
