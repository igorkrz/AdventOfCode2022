from day04.day04 import Day4
import unittest


class TestDay4(unittest.TestCase):

    def test_solutions(self):
        day4 = Day4()
        self.assertEqual(2, day4.part_one())
        self.assertEqual(4, day4.part_two())

        day4.input = day4.custom_input

        self.assertEqual(507, day4.part_one())
        self.assertEqual(897, day4.part_two())


if __name__ == "__main__":
    unittest.main()
