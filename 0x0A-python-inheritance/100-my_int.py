#!/usr/bin/python3
''' a class MyInt that inherits from int'''


class MyInt(int):
    '''Inherits the builtin int class'''
    def __eq__(self, other):
        '''overides __eq__ (equality) to invert =='''
        return super().__ne__(other)

    def __ne__(self, other):
        '''Overides inequality != to invert != operator'''
        return super().__eq__(other)
