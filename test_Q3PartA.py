import unittest
from Q3PartA import move_direction


class MoveDirectionTest(unittest.TestCase):
    def test_valid_position_and_direction(self):
        # Valid position (2, 3) and valid direction 'NE'
        new_position = move_direction('NE', 2, 3)
        self.assertEqual(new_position, (3, 2))

        # Valid position (5, 6) and valid direction 'S'
        new_position = move_direction('S', 5, 6)
        self.assertEqual(new_position, (5, 7))

        # Valid position (1, 4) and valid direction 'W'
        new_position = move_direction('W', 1, 4)
        self.assertEqual(new_position, (0, 4))

        # Valid position (3, 2) and valid direction 'SE'
        new_position = move_direction('SE', 3, 2)
        self.assertEqual(new_position, (4, 3))

    def test_invalid_position(self):
        # Invalid position (-1, 2)
        with self.assertRaises(ValueError):
            move_direction('N', -1, 2)

        # Invalid position (8, 4)
        with self.assertRaises(ValueError):
            move_direction('E', 8, 4)

        # Invalid position (3, -2)
        with self.assertRaises(ValueError):
            move_direction('S', 3, -2)

        # Invalid position (5, 8)
        with self.assertRaises(ValueError):
            move_direction('W', 5, 8)

    def test_invalid_direction(self):
        # Invalid direction 'ABC'
        with self.assertRaises(ValueError):
            move_direction('ABC', 2, 3)

        # Invalid direction '12'
        with self.assertRaises(ValueError):
            move_direction('12', 5, 6)

        # Invalid direction ''
        with self.assertRaises(ValueError):
            move_direction('', 1, 4)

        # Invalid direction 'SW1'
        with self.assertRaises(ValueError):
            move_direction('SW1', 3, 2)

if __name__ == '__main__':
    unittest.main()
