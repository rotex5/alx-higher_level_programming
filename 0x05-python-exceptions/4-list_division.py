#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    for i, j in zip(my_list_1, my_list_2):
        try:
            div = i/j
            if (isinstance(div, str)) is True:
                raise TypeError

        except ValueError:
            print("wrong type")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        finally:
            new_list.append(div)
    if l1 > l2 or l2 > l1:
        print("out of range")

    while len(new_list) < list_length:
        new_list.append(0)

    return (new_list)
