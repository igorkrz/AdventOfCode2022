from day13.day13 import Day13
import unittest


class TestDay13(unittest.TestCase):

    def test_solutions(self):
        day13 = Day13()
        self.assertEqual(13, day13.part_one())
        self.assertEqual(140, day13.part_two())

        day13.input = day13.custom_input

        self.assertEqual(6428, day13.part_one())
        self.assertEqual(22464, day13.part_two())


if __name__ == "__main__":
    unittest.main()
