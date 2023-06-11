#!/usr/bin/python3

if __name__ == "__main__":
    """ A program that prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    name = dir(hidden_4)
    for i in name:
        if i[:2] != "__":
            print(i)
