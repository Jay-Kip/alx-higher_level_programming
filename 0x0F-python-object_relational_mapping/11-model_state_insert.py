#!/usr/bin/python3
'''adds the State object “Louisiana” to the database '''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''Create database engine'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Create database tables'''
    Base.metadata.create_all(engine)

    '''Create session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Insert new state'''
    newState = State(name='Louisiana')
    session.add(newState)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
