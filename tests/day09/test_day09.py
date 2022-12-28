from day09.day09 import Day9
import unittest


class TestDay9(unittest.TestCase):

    def test_solutions(self):
        day9 = Day9()
        self.assertEqual(13, day9.part_one())
        self.assertEqual(1, day9.part_two())

        day9.input = day9.custom_input

        self.assertEqual(6037, day9.part_one())
        self.assertEqual(2485, day9.part_two())


if __name__ == "__main__":
    unittest.main()
