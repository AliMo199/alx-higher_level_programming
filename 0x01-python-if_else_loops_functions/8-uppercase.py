#!/usr/bin/python3
def uppercase(str):
    """Print string in uppercase."""
    for c1 in str:
        if ord(c1) >= 97 and ord(c1) <= 122:
            c1 = chr(ord(c1) - 32)
        print("{}".format(c1), end="")
    print("")
