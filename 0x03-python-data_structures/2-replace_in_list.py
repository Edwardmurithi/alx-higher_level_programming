#!/usr/bin/pyhton3

def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a
    specific position (like in C)
    """
    for i in range(len(my_list)):
        if idx == i:
            my_list[idx] = element
            return my_list
