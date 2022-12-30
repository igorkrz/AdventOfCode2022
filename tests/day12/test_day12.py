from day12.day12 import Day12
import unittest


class TestDay12(unittest.TestCase):

    def test_solutions(self):
        day12 = Day12()
        self.assertEqual(31, day12.part_one())
        self.assertEqual(29, day12.part_two())

        day12.input = day12.custom_input

        self.assertEqual(330, day12.part_one())
        self.assertEqual(321, day12.part_two())


if __name__ == "__main__":
    unittest.main()
