from day14.day14 import Day14
import unittest


class TestDay14(unittest.TestCase):

    def test_solutions(self):
        day14 = Day14()
        self.assertEqual(24, day14.part_one())
        self.assertEqual(93, day14.part_two())

        day14.input = day14.custom_input

        self.assertEqual(638, day14.part_one())
        self.assertEqual(31722, day14.part_two())


if __name__ == "__main__":
    unittest.main()
