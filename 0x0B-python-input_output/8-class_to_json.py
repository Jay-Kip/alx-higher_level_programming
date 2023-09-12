#!/usr/bin/python3
''' returns the dictionary description with simple data structure'''


def class_to_json(obj):
    '''reaturns the dictionary description'''
    attributes = {}

    for attr, value in obj.__dict__.items():
        if type(value) in [list, dict, str, int, bool]:
            attributes[attr] = value

    return attributes
