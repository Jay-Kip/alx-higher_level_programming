#!/usr/bin/python3

'''Defines a class'''


class Square:
    '''Init a new square'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''getter to current square size'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__value = value

    def area(self):
        '''Return area of the square'''
        return self.__size ** 2
