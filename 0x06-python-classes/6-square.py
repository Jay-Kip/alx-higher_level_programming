#!/usr/bin/python3

'''Definition of a square'''


class Square:
    '''A new square'''
    def __init__(self, size=0, position=(0, 0)):
        '''init a new saquare'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns area of the saquare'''
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for _ in range(0, self.__position[1]):
            print("")
        for _ in range(0, self.__size):
            for _ in range(0, self.position[0]):
                print(" ", end="")
            for _ in range(0, self.__size):
                print("#", end="")
            print("")
