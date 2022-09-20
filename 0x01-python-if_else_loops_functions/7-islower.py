#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if ord(c) is i:
            return True
    else:
        return False
