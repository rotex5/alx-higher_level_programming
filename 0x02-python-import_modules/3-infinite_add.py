#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lenght = len(argv)
    total = 0
    for count in range(1, lenght):
        total += int(argv[count])
    print("{:d}".format(total))
