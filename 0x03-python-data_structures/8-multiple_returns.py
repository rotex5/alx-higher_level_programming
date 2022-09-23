#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        first_character = None
        return (length, first_character)

    first_character = sentence[0]
    return (length, first_character)
