#!/usr/bin/python3
'''Defines class state which inherits from Base'''
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

mt = MetaData()
Base = declarative_base(metadata=mt)


classState(Base):
    """Declares Class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
