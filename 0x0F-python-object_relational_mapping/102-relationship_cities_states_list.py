#!/usr/bin/python3
'''script that lists all City objects from the database '''
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    '''Create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).order_by(State_id):
        for c in i.cities:
            print(c.id, c.name, sep=": ", end="")
            print(" -> " + instance.name)
