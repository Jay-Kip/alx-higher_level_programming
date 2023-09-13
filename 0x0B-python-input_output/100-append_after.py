#!/usr/bin/python3
'''Inserts a line of text to a file'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file'''
    txt = ""
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            txt += line
            if (search_string in line):
                txt += new_string

    with open(filename, "w", encoding="UTF-8") as f:
        f.write(txt)
