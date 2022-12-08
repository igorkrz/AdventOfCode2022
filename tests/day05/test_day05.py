from day05.day05 import Day5
import unittest


class TestDay5(unittest.TestCase):

    def test_solutions(self):
        day5 = Day5()
        self.assertEqual('CMZ', day5.part_one())
        self.assertEqual('MCD', day5.part_two())

        day5.input = day5.custom_input

        self.assertEqual('WCZTHTMPS', day5.part_one())
        self.assertEqual('BLSGJSDTS', day5.part_two())


if __name__ == "__main__":
    unittest.main()
