from typing import List, Type
from project.animals.animal import Bird
from project.food import Food
from project.food import Meat
from project.food import Vegetable
from project.food import Fruit
from project.food import Seed

class Owl(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]
    @property
    def weight_coefficient(self):
        return 0.25
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

class Hen(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Fruit, Vegetable, Seed]
    @property
    def weight_coefficient(self):
        return 0.35
    @staticmethod
    def make_sound():
        return "Cluck"