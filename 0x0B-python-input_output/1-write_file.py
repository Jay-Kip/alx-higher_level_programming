#!/usr/bin/python3
'''Writes to a file'''


def write_file(filename="", text=""):
    '''Writes text to a file'''
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
