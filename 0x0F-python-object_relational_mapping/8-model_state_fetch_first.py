#!/usr/bin/python3
'''8-model_state_fetch_first.py'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysldb://{}: {}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2]. sys.atgv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
