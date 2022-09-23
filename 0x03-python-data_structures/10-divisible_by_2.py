#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    t = True
    f = False
    outcome = []

    for i in my_list:
        if i % 2 == 0:
            outcome.append(t)
        else:
            outcome.append(f)
    return outcome
