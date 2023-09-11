#!/usr/bin/python3
''' a class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        self.__size = value

    def area(self):
        return int(self.__size) * 4
