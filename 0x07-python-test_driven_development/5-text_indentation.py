#!/usr/bin/python3
"""
Module includes a function that prints
 text.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each
    of these characters: . ? and :
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")

    new_text = text.replace('. ', '.\n\n')
    new_text = new_text.replace('? ', '?\n\n')
    new_text = new_text.replace(': ', ':\n\n')
    print(new_text)
