#!/usr/bin/python3
# print_comb2.py
# a program that prints numbers from 0 to 99
for i in range(0, 100):
    if i == 99:
        print(f"{i}")
    else:
        print(f"{i:02d}", end=", ")
