from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Rex", "dog", "Woff")
    def test_init(self):
        self.assertEqual("Rex", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("Woff", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Rex makes Woff", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Rex is of type dog", self.mammal.info())

if __name__ == "__main__":
    main()