from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption    #in liters per km
    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    AC_CONSUMPTION = 0.9
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_COEFFICIENT = 0.95
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_COEFFICIENT