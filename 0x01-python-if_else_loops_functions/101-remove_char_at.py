#!/usr/bin/python3

def remove_char_at(str, n):
    start = str[:n]
    end = str[n + 1:]
    return start + end
