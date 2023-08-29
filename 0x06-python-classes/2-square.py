#!/usr/bin/python3


'''Class Aquare that defines a square by: (based on 1-square.py)'''


class Square:
    def __init__(self, size=0):

        '''Isinstance Here  checks if size is int'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
