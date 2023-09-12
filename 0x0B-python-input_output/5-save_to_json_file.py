#!/usr/bin/python3
'''Writes an object to a text file, using a JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    '''writes to a text file'''
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
