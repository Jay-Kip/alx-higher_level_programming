#!/usr/bin/python3
'''lists all State objects that contain the letter a from the database '''
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    '''Creating database engine'''
    engine = create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Creating database tables'''
    Base.metadata.create_all(engine)

    '''creates session'''
    Session - sessionmaker(bind=engine)
    session = Session()

    '''Queryin the database and printing result'''
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
