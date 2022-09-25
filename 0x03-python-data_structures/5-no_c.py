#!/usr/bin/env python3

def no_c(my_string):
    length = len(my_string)
    output = ""

    for i in range(length):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        output += my_string[i]

    return output
