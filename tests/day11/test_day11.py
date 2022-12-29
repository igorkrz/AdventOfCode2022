from day11.day11 import Day11
import unittest


class TestDay11(unittest.TestCase):

    def test_solutions(self):
        day11 = Day11()
        self.assertEqual(10605, day11.part_one())
        self.assertEqual(2713310158, day11.part_two())

        day11.input = day11.custom_input

        self.assertEqual(76728, day11.part_one())
        self.assertEqual(21553910156, day11.part_two())


if __name__ == "__main__":
    unittest.main()
