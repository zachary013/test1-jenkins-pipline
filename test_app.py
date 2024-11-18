import unittest
from app import add, subtract, circle_area

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 3), -3)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)
        with self.assertRaises(ValueError):
            circle_area(-1)

if __name__ == "__main__":
    unittest.main()
