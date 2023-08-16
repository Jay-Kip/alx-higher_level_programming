#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary.keys())  # Order items using keys
    lst.sort()  # For sorting the keys

    for i in lst:  # Iterate over the keys
        print("{}: {}".format(i, a_dictionary.get(i)))
