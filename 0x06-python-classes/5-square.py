#!/usr/bin/python3
'''Defines another square'''


class Square:
    '''init a class square'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''getter/setter of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return area of the square'''
        return self.size ** 2

    def my_print(self):
        '''Prints the square using '#' '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
