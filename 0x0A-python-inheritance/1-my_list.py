#!/usr/bin/python3
'''Class that inherits from list'''


class MyList(list):
    '''inherits from list'''
    def print_sorted(self):
        '''Prints a sorted list'''
        print(sorted(self))
