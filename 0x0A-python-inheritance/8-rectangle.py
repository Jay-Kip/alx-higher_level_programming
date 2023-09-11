#!/usr/bin/pyton3
''' a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        self.__height = value
