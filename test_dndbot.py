import unittest
from unittest.mock import patch
import dndbot



class TestCharacterClass(unittest.TestCase):
    def test_set_attribute(self):
        self.assertEqual(dndbot.Character.set_attribute(self, 'Strength', 1), (1, -5))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Strength', 2), (2, -4))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Strength', 3), (3, -4))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Strength', 4), (4, -3))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Strength', 5), (5, -3))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Dexterity', 6), (6, -2))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Dexterity', 7), (7, -2))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Dexterity', 8), (8, -1))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Dexterity', 9), (9, -1))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Dexterity', 10), (10, 0))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Constitution', 11), (11, 0))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Constitution', 12), (12, 1))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Constitution', 13), (13, 1))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Constitution', 14), (14, 2))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Constitution', 15), (15, 2))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Intelligence', 16), (16, 3))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Intelligence', 17), (17, 3))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Intelligence', 18), (18, 4))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Intelligence', 19), (19, 4))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Intelligence', 20), (20, 5))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Wisdom', 21), (21, 5))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Wisdom', 22), (22, 6))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Wisdom', 23), (23, 6))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Wisdom', 24), (24, 7))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Wisdom', 25), (25, 7))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Charisma', 26), (26, 8))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Charisma', 27), (27, 8))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Charisma', 28), (28, 9))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Charisma', 29), (29, 9))
        self.assertEqual(dndbot.Character.set_attribute(self, 'Charisma', 30), (30, 10))
        





if __name__ == '__main__':
    unittest.main()
