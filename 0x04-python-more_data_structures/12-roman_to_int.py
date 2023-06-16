#!/usr/bin/python3
# 12-roman_to_int.py
# by: Aropet_Joel

def to_subtract(list_num):
    """A function def roman_to_int(roman_string): that converts
    a Roman numeral to an integer.
    """
    max_num = max(list_num)
    sub = 0

    for i in list_num:
        if max_num > i:
            sub += i

    return (max_num - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_the_keys = list(rom_n.keys())

    x = 0
    list_x = [0]
    last_roman = 0

    for ch in roman_string:
        for r_x in list_the_keys:
            if r_x == ch:
                if rom_n.get(ch) <= last_roman:
                    x += to_subtract(list_x)
                    list_x = [rom_n.get(ch)]
                else:
                    list_x.append(rom_n.get(ch))

                last_roman = rom_n.get(ch)

    x += to_subtract(list_x)

    return (x)
