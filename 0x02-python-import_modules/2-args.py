#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length: int = len(argv) - 1
    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length))
        for count, value in enumerate(argv):
            if count == 0:
                continue
            print("{:d}: {}".format(count, value))
