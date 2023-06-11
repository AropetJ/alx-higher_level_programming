#!/usr/bin/python3

if __name__ == "__main__":
    """ A program that prints the result of the addition of all arguments"""

    import sys

    i = 0
    for j in range(len(sys.argv) - 1):
        i += int(sys.argv[j + 1])
    x = "{}"
    print(x.format(i))
