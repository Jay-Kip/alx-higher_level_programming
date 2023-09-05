#!/usr/bin/python3
''' Defines a class LockedClass'''


class LockedClass:
    '''Prevents users from instantiating new Lockedclass attributes
    for anything but attributes called 'first_name'''
    __slots__ = ['first_name']
