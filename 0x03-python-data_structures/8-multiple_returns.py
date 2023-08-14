#!/usr/bin/python3

def multiple_returns(sentence):
    for char in sentence:
        return len(sentence), char
