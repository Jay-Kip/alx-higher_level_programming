#!/usr/bin/python3
'''Checks for Largest number'''


def find_peak(list_of_integers):
    '''Returns largest number in an array'''
    try:
        list_of_integers.sort()
        return list_of_integers[-1]
    except IndexError:
        return 'None'
