#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:  # Checks if key is present
        del a_dictionary[key]  # Deletes the key with it's value
    return a_dictionary
