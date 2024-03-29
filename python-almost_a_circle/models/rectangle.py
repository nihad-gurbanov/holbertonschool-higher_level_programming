#!/usr/bin/python3
''' Rectangle Module Doc '''


from models.base import Base


class Rectangle(Base):
    ''' Rectangle Class Doc '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value, True)
        self.__y = value

    def validator(self, name, value, zero_value=False):
        '''This function validates given arguments'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not zero_value and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if zero_value and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Area method returns area of rectangle'''
        return self.width * self.height

    def display(self):
        '''Display method displays rectangles by hash character'''
        for y_ in range(self.y):
            print()
        for i in range(self.height):
            for x_ in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''Str prints the object in customized version'''
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''Update method assigns an argument to each attribute'''
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        else:
            attributes = ["id", "width", "height", "x", "y"]

            for attribute in attributes:
                if attribute in kwargs:
                    try:
                        setattr(self, attribute, kwargs[attribute])
                    except Exception:
                        pass

    def to_dictionary(self):
        ''' This returns the dictionary representation of a Rectangle'''
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
