from typing import List, Type
from project.animals.animal import Mammal
from project.food import Food
from project.food import Meat
from project.food import Seed
from project.food import Fruit
from project.food import Vegetable


class Mouse(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Fruit, Vegetable]
    @property
    def weight_coefficient(self):
        return 0.1
    @staticmethod
    def make_sound():
        return "Squeak"

class Dog(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]
    @property
    def weight_coefficient(self):
        return 0.4
    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]
    @property
    def weight_coefficient(self):
        return 0.3
    @staticmethod
    def make_sound():
        return "Meow"

class Tiger(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]
    @property
    def weight_coefficient(self):
        return 1
    @staticmethod
    def make_sound():
        return "ROAR!!!"