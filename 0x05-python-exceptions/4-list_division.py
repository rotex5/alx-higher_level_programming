#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
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
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)

    # while len(new_list) < list_length:
        # new_list.append(0)

    return (new_list)
