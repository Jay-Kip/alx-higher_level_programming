#!/usr/bin/python3
'''prints the State object with the name passed
as argument from the database '''
import sys
from model_base import Base, State
from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''Create database engine'''
    engine = create_engine('mysql+mysqldb://():()$localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create database tables'''
    Base.metadata.create_all(engine)

    '''create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Querrying the database and printing results'''
    match = session.query(State).filter(State.name == (sys.argv[4], ))
    try:
        print(match[0].id)
    except IndexError:
        print("Not Found")
