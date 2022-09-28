#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    new_set = set()
    for i in set_1:
        for j in set_2:
            if i in set_2 or j in set_1:
                continue
            else:
                new_set.add(i)
                new_set.add(j)
    return new_set
    """
    return set_1 ^ set_2
