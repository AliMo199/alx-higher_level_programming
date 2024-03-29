#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): number of elements to divide.

    Returns:
        new list of length list_length containing all divisions.
    """
    new_list = []
    for n in range(0, list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
