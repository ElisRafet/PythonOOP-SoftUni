class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_consumed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_consumed:
            self.fuel -= fuel_consumed

