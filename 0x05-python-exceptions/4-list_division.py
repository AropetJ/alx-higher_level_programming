#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 lists.

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): The number of integers in the lists to divide.

    Returns:
        A new list (length = list_length) with all divisions.
    """
    temp_list = []
    for j in range(0, list_length):
        try:
            div = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            temp_list.append(div)
    return (temp_list)
