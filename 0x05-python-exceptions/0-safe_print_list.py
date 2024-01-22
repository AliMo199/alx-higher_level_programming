#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x element of list.

    Args:
        my_list (list): list to print element from.
        x (int): number of element of my_list to print.

    Returns:
        number of element printed.
    """
    ret = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
