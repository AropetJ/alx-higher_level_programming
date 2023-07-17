#!/usr/bin/python3
# rectangle.py
""" Defines a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ My rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialising class attributes

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the width of the rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the cordinate x of the rectangle """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Sets the cordinate x of the rectangle """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Sets the cordinate y of the rectangle """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Sets the cordinate y of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ A function that returns the area of a rectangle """
        return (self.height * self.width)

    def display(self):
        """ A function that prints the rectangle using the '#'"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ A human readable representation of a class """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """A function that in none and keyword arguments.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            num_args = 0
            for i in args:
                if num_args == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif num_args == 1:
                    self.width = i
                elif num_args == 2:
                    self.height = i
                elif num_args == 3:
                    self.x = i
                elif num_args == 4:
                    self.y = i
                num_args += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ A function that returns a dictionary representation of
            a rectangle
        """
        return ({
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        })
