from unittest import TestCase, main
from project.hero import Hero

class TestHero(TestCase):
    username = "Cleopatra"
    health = 15.5
    damage = 1.5
    level = 27

    def setUp(self):
        self.hero = Hero(self.username, self. level, self.health, self.damage)
        self.enemy = Hero("Cleo", 10,5, 2)
    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_battle_equal_enemy_name(self):
        self.enemy.username = self.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        self.hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_zero_or_less(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Cleo. He needs to rest", str(ex.exception))
        self.enemy.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Cleo. He needs to rest", str(ex.exception))
    # error
    def test_battle_draw(self):
        self.enemy.health = self.health
        self.enemy.damage = self.damage
        self.enemy.level = self.level
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_hero_win(self):
        self.enemy.health = 1
        self.enemy.damage = 1
        self.enemy.level = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)

    def test_battle_hero_lose(self):
        self.hero.health = 2
        self.hero.damage = 2
        self.hero.level = 2
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)

    def test__str(self):
        result = self.hero.__str__()
        self.assertEqual(f"Hero Cleopatra: 27 lvl\n" \
               f"Health: 15.5\n" \
               f"Damage: 1.5\n", result)

if __name__ == "__main__":
    main()