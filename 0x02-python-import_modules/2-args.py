#!/usr/bin/python3

if __name__ == "__main__":
    """  a program that prints the number of and the list of its arguments"""
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument.")
    else:
        x = "{} arguments:"
        print(x.format(i))
    for j in range(i):
        y = "{}:{}"
        print(y.format(j + 1, sys.argv[j + 1]))
