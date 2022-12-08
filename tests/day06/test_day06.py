from day06.day06 import Day6
import unittest


class TestDay6(unittest.TestCase):

    def test_solutions(self):
        day6 = Day6()
        self.assertEqual(7, day6.part_one())
        self.assertEqual(19, day6.part_two())

        day6.input = day6.custom_input

        self.assertEqual(1640, day6.part_one())
        self.assertEqual(3613, day6.part_two())


if __name__ == "__main__":
    unittest.main()
