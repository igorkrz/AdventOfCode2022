from day03.day03 import Day3
import unittest


class TestDay2(unittest.TestCase):

    def test_solutions(self):
        day3 = Day3()
        self.assertEqual(157, day3.part_one())
        self.assertEqual(70, day3.part_two())

        day3.input = day3.custom_input

        self.assertEqual(7428, day3.part_one())
        self.assertEqual(2650, day3.part_two())


if __name__ == "__main__":
    unittest.main()
