#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    for char in sentence:
        return ((len(sentence)), char)
