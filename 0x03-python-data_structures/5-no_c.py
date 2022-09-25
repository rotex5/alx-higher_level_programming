#!/usr/bin/env python3

def no_c(my_string):
    # return my_string.translate({ord(i): None for i in 'cC'})
    length = len(my_string)
    output = ""

    for i in range(length):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        output += my_string[i]

    return output
