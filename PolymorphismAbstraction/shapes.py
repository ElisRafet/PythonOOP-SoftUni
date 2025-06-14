from abc import ABC, abstractmethod
import math

class Shapes(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shapes):
    def __init__(self, r):
        self.__r = r

    def calculate_area(self):
        return math.pi * self.__r * self.__r

    def calculate_perimeter(self):
        return 2 * math.pi * self.__r

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def calculate_area(self):
        return self.__width * self.__height


