#!/usr/bin/python3

def weight_average(my_list=[]):
    numerator_total = 0
    denominator_total = 0
    rows = len(my_list)
    cols = len(my_list[0])

    for i in range(rows):
        sub = 1
        for j in range(cols):
            sub *= my_list[i][j]
        numerator_total += sub

    for i in range(rows):
        denominator_total += my_list[i][-1]

    return numerator_total/denominator_total
