#!/usr/bin/python3

def search_replace(my_list, search, replace):
    len_ = len(my_list)
    new_list = my_list.copy()

    for i in range(len_):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
