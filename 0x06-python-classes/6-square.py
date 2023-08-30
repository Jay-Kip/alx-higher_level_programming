#!/usr/bin/python3

'''Definition of a square'''


class Square:
    '''A new square'''
    def __init__(self, size=0, position=(0, 0)):
        '''init a new saquare'''
        self.__size = size
        self.__position = position

    @property
    '''getter/setter of the square'''
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''getter/setter of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns area of the saquare'''
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.__position[0] + "#" * self.__size)
