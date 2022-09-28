#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # return {key:val for key, val in a_dictionary.items() if val != value}
    for key, val in dict(a_dictionary).items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
