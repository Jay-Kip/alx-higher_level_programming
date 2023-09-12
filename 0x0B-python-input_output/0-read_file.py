#!/usr/bin/python3
'''Function that reads a text file'''


def read_file(filename=""):
    '''Reads a file'''
    with open(filename, encoding="UTF-8") as f:
        f.read()
