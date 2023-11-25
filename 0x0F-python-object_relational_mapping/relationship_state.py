#!/usr/bin/python3
'''Declares a class State as Base'''
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mt = MetaData()
Base = declarative_base(metadata=mt)


class State(Base):
    '''Declares class state'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
