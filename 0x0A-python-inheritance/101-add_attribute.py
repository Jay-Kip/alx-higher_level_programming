#!/usr/bin/python3
''' a function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attribute, val):

    '''adds attribute to an onject if possible'''

    if not hasattr(obj, "__dict__"):
        '''checks to see if new attribute can be added'''
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, val)
