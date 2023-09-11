#!/usr/bin/python3
''' a class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''defines a class Rectangle'''
    def __init__(self, size):
        '''initializes an instance of the class'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
