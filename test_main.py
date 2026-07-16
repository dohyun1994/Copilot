import unittest

from main import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_adds_two_positive_integers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_and_positive_numbers(self):
        self.assertEqual(add_numbers(-1, 5), 4)

    def test_adds_floats(self):
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)


if __name__ == "__main__":
    unittest.main()
