#!/usr/bin/python3
'''
This is a module for adding integers
Returns:
    int: Sum of 'a' and  'b'
'''
def add_integer(a, b=98):
    '''
    Adds two integers, 'a' and 'b'
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
