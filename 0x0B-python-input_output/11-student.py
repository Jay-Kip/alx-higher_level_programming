#!/usr/bin/python3
'''Defines a class Stident'''


class Student:
    '''Defines a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) in [list] and all(type(k) in [str] for k in attrs)):
            return {p: getattr(self, p) for p in attrs if hasattr(self, p)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
