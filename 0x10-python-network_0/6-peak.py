#!/usr/bin/python3
'''Checks for Largest number'''


def find_peak(list_of_integers):
    try:
        return max(list_of_integers)
    except ValueError:
        return 'None'
