from day01.day01 import Day1
import unittest


class TestDay1(unittest.TestCase):

    def test_solutions(self):
        day1 = Day1()
        self.assertEqual(24000, day1.part_one())
        self.assertEqual(45000, day1.part_two())

        day1.input = day1.custom_input

        self.assertEqual(70296, day1.part_one())
        self.assertEqual(205381, day1.part_two())


if __name__ == "__main__":
    unittest.main()
