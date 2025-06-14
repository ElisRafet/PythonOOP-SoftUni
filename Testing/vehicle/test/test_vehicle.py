from unittest import TestCase, main
from project.vehicle import Vehicle

class TestVehicle(TestCase):

    fuel = 40.5
    horse_power = 125.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)
    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_less_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(28, self.vehicle.fuel)

    def test_refuel_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successfully(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(20)
        self.assertEqual(30, self.vehicle.fuel)

    def test__str(self):
        self.assertEqual(f"The vehicle has 125.5 " \
                         f"horse power with 40.5 fuel left and " \
                         f"1.25 fuel consumption", self.vehicle.__str__())

if __name__ == "__main__":
    main()