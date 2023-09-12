#!/usr/bin/python3
'''Defines a class student'''


class Student:
    '''Defines a class student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        attributes = {}

        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes
