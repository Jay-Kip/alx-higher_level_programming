#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()  # Makes a copy of the dictionary
    lst = list(copy_dict.keys())  # Convert dictionary to a list

    for i in lst:  # Itterate over the dictionary
        copy_dict[i] *= 2

    return copy_dict
