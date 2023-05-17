import unittest
from Q3PartB import fastest_racer

class FastestRacerTest(unittest.TestCase):
    def test_valid_input_lower_boundary(self):
        result = fastest_racer("Racer 1", "Racer 2", 2, 1, 1, 1)
        self.assertEqual(result, "Racer 2")

    def test_invalid_input_below_lower_boundary(self):
        result = fastest_racer("Racer 1", "Racer 2", 0, 0, 0, 0)
        self.assertEqual(result, "Invalid Input")

    def test_valid_input_at_lower_boundary(self):
        result = fastest_racer("Racer 1", "Racer 2", 0.0001, 0.0001, 0.0001, 0.0001)
        self.assertEqual(result, "Tie")

    def test_valid_input_at_tie_boundary(self):
        result = fastest_racer("Racer 1", "Racer 2", 100, 100, 100, 100)
        self.assertEqual(result, "Tie")

if __name__ == '__main__':
    unittest.main()
