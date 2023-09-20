# File: test_gratitudes.py

import unittest
from lib.gratitudes import Gratitudes

class TestGratitudes(unittest.TestCase):

    def test_add_gratitude(self):
        gratitude_list = Gratitudes()
        gratitude_list.add("Family")
        gratitude_list.add("Health")
        gratitude_list.add("Friendship")

        self.assertEqual(gratitude_list.gratitudes, ["Family", "Health", "Friendship"])

    def test_format_gratitudes(self):
        gratitude_list = Gratitudes()
        gratitude_list.add("Nature")
        gratitude_list.add("Love")

        formatted = gratitude_list.format()
        expected_output = "Be grateful for: Nature, Love"

        self.assertEqual(formatted, expected_output)

if __name__ == '__main__':
    unittest.main()
