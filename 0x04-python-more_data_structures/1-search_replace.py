#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function replaces all occurrences
    of an element by another in new list
    """
    new_list = []
    for elmnt in my_list:
        if elmnt == search:
            new_list.append(replace)
        else:
            new_list.append(elmnt)
    return new_list
