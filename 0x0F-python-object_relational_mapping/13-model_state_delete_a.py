#!/usr/bin/python3
'''deletes all State objects with a name
containing the letter a from the database '''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    '''create database engine'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create tables'''
    Base.metadata.create_all(engine)

    '''Create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Delete instance from the database'''
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
