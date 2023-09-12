#!/usr/bin/python3
'''Script that adds all args to a Python list'''
import sys
import json


def save_to_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


'''Add arguements to a list'''
arguements = sys.argv[1:]
filename = "add_item.json"

'''load existing data from file'''
try:
    existing_data = load_from_json_file(filename)
except FileNotFoundError:
    existing_data = []

'''Add new arguements to the existing data'''
existing_data.extend(arguements)

'''Save the updated data to the file'''
save_to_json_file(filename, existing_data)
