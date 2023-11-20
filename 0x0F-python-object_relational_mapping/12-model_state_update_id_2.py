#!/usr/bin/python3
'''changes the name of a State object from the database '''
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    '''create database engine'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create tables'''
    Base.metadata.create_all(engine)

    '''create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''change the name of the state object'''
    new = session.query(State).filter_by(id=2).first()
    new.name = 'New Mexico'
    session.commit()
