from day08.day08 import Day8
import unittest


class TestDay8(unittest.TestCase):

    def test_solutions(self):
        day8 = Day8()
        self.assertEqual(21, day8.part_one())
        self.assertEqual(8, day8.part_two())

        day8.input = day8.custom_input

        self.assertEqual(1711, day8.part_one())
        self.assertEqual(301392, day8.part_two())


if __name__ == "__main__":
    unittest.main()
