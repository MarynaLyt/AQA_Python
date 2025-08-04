from abc import ABC, abstractmethod


class figure(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    def __str__(self):
        return f"Name: {self.area}, Salary: {self.perimeter}"


class rectangle(figure, ABC):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Width: {self.__width}, height: {self.__height}"

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2


class square(figure, ABC):
    def __init__(self, side: int):
        self.__side = side

    def __str__(self):
        return f"Side: {self.__side}"

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class rhombus(figure, ABC):
    def __init__(self, d1, d2, side):
        self.__d1 = d1
        self.__d2 = d2
        self.__rhombus_side = side

    def __str__(self):
        return f"First diagonal: {self.__d1}, second diagonal: {self.__d2}, and side: {self.__rhombus_side}"

    def area(self):
        return (self.__d1 * self.__d2) / 2

    def perimeter(self):
        return self.__rhombus_side * 4


figures: list = [rectangle(5, 3), square(4), rhombus(6, 8, 5)]

for figure in figures:
    print(f"Figure: {figure.__class__.__name__}")
    print(f"  Area: {figure.area()}")
    print(f"  Perimeter: {figure.perimeter()}\n")