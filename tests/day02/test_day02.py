from day02.day02 import Day2
import unittest


class TestDay2(unittest.TestCase):

    def test_solutions(self):
        day2 = Day2()
        self.assertEqual(15, day2.part_one())
        self.assertEqual(12, day2.part_two())

        day2.input = day2.custom_input

        self.assertEqual(13484, day2.part_one())
        self.assertEqual(13433, day2.part_two())


if __name__ == "__main__":
    unittest.main()
