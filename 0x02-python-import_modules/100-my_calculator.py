#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    lenght = len(argv)
    operators = ["+", "-", "*", "/"]

    if lenght != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = str(argv[2])
    output = "{} {} {} = {}"

    if op in operators:
        if op == "-":
            print(output.format(a, op, b, sub(a, b)))
        elif op == "*":
            print(output.format(a, op, b, mul(a, b)))
        elif op == "+":
            print(output.format(a, op, b, add(a, b)))
        elif op == "/":
            print(output.format(a, op, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
