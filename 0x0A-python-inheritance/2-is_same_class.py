#!/usr/bin/python3
'''Checks if object is exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    '''Returns true or false depending if is instance of class'''
    return type(obj) is a_class
