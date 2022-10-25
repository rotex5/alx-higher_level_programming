#!/usr/bin/python3
""" Includes a `write_file` function"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as a_file:
        charCount = a_file.write(text)
    return charCount
