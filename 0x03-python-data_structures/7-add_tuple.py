#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = []
    tuple_a = list(tuple_a) + [0]*2
    tuple_b = list(tuple_b) + [0]*2
    for (i, x) in zip(tuple_a, tuple_b):
        t.append((i+x))
    t_change = tuple(t)[0:2]
    return t_change
