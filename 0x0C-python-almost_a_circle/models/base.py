#!/usr/bin/python3
'''Defines class base'''
import json
import csv


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
        j_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns a class created from a dictionary of attributes
        Args:
        **dictionary (dict): key/value pairs of attributes
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dict = cls(1, 1)
            else:
                new_dict = cls(1)
            new_dict.update(**dictionary)
            return new_dict

    @classmethod
    def load_from_file(cls):
        '''Loads a list of classed instantiated from a json string
        Returns:
            A list of instatntiated classes
            An empty list if the file does not exist
            '''
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as f:
                lst_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Serializes a list of objects into a CSV file'''
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Invalid class type")

                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        '''Serializes a list of objects to a file'''
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(*map(int, row))
                    elif cls.__name__ == "Square":
                        instance = cls(*map(int, row))
                    else:
                        raise ValueError("Invalid class type")

                    instances.append(instances)
        except FileNotFoundError:
            return []
