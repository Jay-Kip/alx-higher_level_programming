#!/usr/bin/python3
'''Returns true if the object is an instance of the class it inherited from'''


def inherits_from(obj, a_class):
    '''Checks if is instance'''
    if type(obj) in [a_class]:
        return False
    return issubclass(type(obj), a_class)
