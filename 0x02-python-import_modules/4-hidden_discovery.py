#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 modul."""
    import hidden_4

    names_h = dir(hidden_4)
    for name in names_h:
        if name[:2] != "__":
            print(name)
