#!/usr/bin/python3
'''class based onm 6-base_geometry'''


class BaseGeometry:

    '''Defines the class'''

    def area(self):
        '''raises exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value to be int or > 0'''
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.__name = value
