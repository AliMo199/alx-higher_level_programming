#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print first x element of a list that are integers.

    Args:
        my_list (list): list to print element from.
        x (int): number of element of my_list to print.

    Returns:
        number of element printed.
    """
    ret = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
