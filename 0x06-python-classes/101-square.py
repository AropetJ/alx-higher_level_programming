#!/usr/bin/python3
# 101-square.py
"""Define a class Square"""


class Square():
    """A class Square that defines a square by: (based on 5-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the attributes of a square

        Args:
            position (int, int): The position of the square
            size (int): Private instance attribute
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retriving the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieving the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square of the # character."""
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Defines the print() representation of a square."""
        result = ""
        if self.__size != 0:
            result += "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result
