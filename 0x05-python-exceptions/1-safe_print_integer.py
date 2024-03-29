#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with "{:d}".format().

    Args:
        value (int): integer to print.

    Returns:
        If a TypeError or ValueError occur - False.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
