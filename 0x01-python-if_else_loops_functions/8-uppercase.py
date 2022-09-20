#!/usr/bin/python3
def uppercase(str):
    output=''
    for alpha in str:
        alpha = ord(alpha)
        if alpha >=65 and alpha <= 90:
            output += chr(alpha)
        elif alpha >= 97 and alpha <= 122:
            output += chr(alpha - 32)
        else:
            output += chr(alpha)
    print('{}'.format(output))
