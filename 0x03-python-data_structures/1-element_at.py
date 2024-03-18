#!/usr/bin/python3

def element_at(my_list, idx):
    """function that retrieves an element from a list like in C
    """
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
