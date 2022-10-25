#!/usr/bin/python3
""" Includes a `write_file` function"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, mode='a', encoding="utf-8") as a_file:
        charCount = a_file.write(text)
    return charCount
