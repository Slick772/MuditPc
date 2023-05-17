import unittest
from unittest.mock import patch
from io import StringIO
from Q3PartC import pie_divider


class PieDividerTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_positive_case(self, mock_stdout):
        user_input = ['5', '20']
        expected_output = "4\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_zero_people(self, mock_stdout):
        user_input = ['0', '20', '4', '16']
        expected_output = "Invalid\n4\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_people(self, mock_stdout):
        user_input = ['-5', '20', '4', '16']
        expected_output = "Invalid\n4\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_pies(self, mock_stdout):
        user_input = ['5', '-20', '4', '16']
        expected_output = "Invalid\n4\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_single_person(self, mock_stdout):
        user_input = ['1', '20']
        expected_output = "20\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_more_people_than_pies(self, mock_stdout):
        user_input = ['10', '5']
        expected_output = "0\n5\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input_after_invalid(self, mock_stdout):
        user_input = ['0', '0', '4', '16']
        expected_output = "Invalid\n4\n0\nPerfect\n"
        with patch('builtins.input', side_effect=user_input):
            pie_divider()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
