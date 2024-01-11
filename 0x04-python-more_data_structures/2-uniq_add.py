#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function adds all unique
    integers in list (only once for each integer)
    """
    new_list = []
    sum = 0
    for nums in my_list:
        if nums not in new_list:
            sum += nums
            new_list.append(nums)
    return sum
