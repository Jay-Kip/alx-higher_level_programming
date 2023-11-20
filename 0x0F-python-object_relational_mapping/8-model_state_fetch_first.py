#!/usr/bin/python3
'''8-model_state_fetch_first.py'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''Creating database engine'''
    engine = create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Creating tables defined in the Base class'''
    Base.metadata.create_all(engine)

    '''Creating a session bound to the db engine'''
    Session = sessionmaker(bind=engine)
    '''CReating a session object'''
    session = Session()

    '''Performing a database query and print result'''
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
