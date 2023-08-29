#!/usr/bin/python3

'''Define a class 'Square' '''


class Square:

    '''A square'''
    def __init__(self, size=0):
        '''Initiazlizes a new square'''
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns area of the square'''
        return self.__size ** 2
