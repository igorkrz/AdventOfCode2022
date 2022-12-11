from day07.day07 import Day7
import unittest


class TestDay7(unittest.TestCase):

    def test_solutions(self):
        day7 = Day7()
        self.assertEqual(95437, day7.part_one())
        self.assertEqual(24933642, day7.part_two())

        day7.input = day7.custom_input

        self.assertEqual(1350966, day7.part_one())
        self.assertEqual(6296435, day7.part_two())


if __name__ == "__main__":
    unittest.main()
