from unittest import TestCase, main

class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



from unittest import TestCase, main

class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Vasko", 101, 2)
    def test_init(self):

        self.assertEqual("Vasko", self.worker.name)
        self.assertEqual(101, self.worker.salary)
        self.assertEqual(2, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_zero_raising_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_negative_raising_exception(self):
        self.worker.energy = -2
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(-2, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_positive_raising_exception(self):
        self.worker.money = 101
        self.worker.energy = 3
        self.worker.work()
        self.assertEqual(2, self.worker.energy)
        self.assertEqual(202, self.worker.money)

    def test_rest(self):
        self.worker.energy = 3
        self.worker.rest()
        self.assertEqual(4, self.worker.energy)

    def test_get_info(self):
        self.worker.money = 50
        result = self.worker.get_info()
        self.assertEqual('Vasko has saved 50 money.', result)


if __name__ == "__main__":
    main()



