#!/usr/bin/python3
'''Defines class base'''
import json


class Base:
    '''Defines a class base'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''Initializes a new instance of class base'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)
