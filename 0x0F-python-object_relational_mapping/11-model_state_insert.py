10-model_state_my_get.py

#!/usr/bin/python3
""" adds the state object 'Louisiana' to the database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqalchemy import create_engine


if __name__ == "__main__":
    '''Create database engine'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create tables'''
    Base.metadata.create_all(engine)

    '''Creating session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Creating new object state'''
    newState = State(name='Louisiana')
    session.add(newState)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()

