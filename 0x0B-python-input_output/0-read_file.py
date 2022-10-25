#!/usr/bin/python3

def read_file(filename=""):
    """ reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as new_file:
        for line in new_file:
            print(line, end="")
