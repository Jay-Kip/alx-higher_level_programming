#!/usr/bin/python3
'''Creates an object file from a JSON file'''
import json


def load_from_json_file(filename):
    '''Creates an object file from a json file'''
    with open(filename, "r", encoding="UTF-8") as file:
        json_data = file.read()
        return json.loads(json_data)
