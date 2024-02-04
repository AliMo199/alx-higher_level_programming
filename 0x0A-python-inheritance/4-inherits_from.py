#!/usr/bin/python3
"""Define inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if object is inherited instance of class.

    Args:
        obj (any): object to check.
        a_class (type): class to match type of obj to.
    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
