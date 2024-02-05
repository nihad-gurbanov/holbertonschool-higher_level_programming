#!/usr/bin/python3
'''
    Rectangle Module defines a rectangle
'''


class Rectangle:
    '''
        Rectangle Class
    '''

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value