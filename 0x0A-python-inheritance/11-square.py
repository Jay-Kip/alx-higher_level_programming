#!/usr/bin/python3
'''A class Square that inherits from rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''defines a class Square'''
    def __init__(self, size):
        '''initializes a new instance'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''Print string representation'''
        return "[Square] {}/{}".format(self.__size, self.__size)
