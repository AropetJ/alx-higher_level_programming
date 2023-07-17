#!/usr/bin/python3
# square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """ My square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialising class attributes
        Args:
            size (int): The size of the Square.
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The identity of the Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ A function that takes in none and keyword arguments

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ A function that returns the dictionary representation
        of a square
        """
        return ({
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        })
