#!/usr/bin/python3
'''Creates the State "California" with the City "San Francisco'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                   pool_pre_ping=True))

    Base.metadata.create_all(engine)

    '''Create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Create new city and state'''
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    '''Add and commit new city and state'''
    session.add(newState)
    session.add(newCity)
    session.commit()
