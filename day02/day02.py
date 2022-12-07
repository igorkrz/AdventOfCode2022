from utils.utils import Utils


class Day2(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        outcomes = {
            'A X': 4,
            'A Y': 8,
            'A Z': 3,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 7,
            'C Y': 2,
            'C Z': 6,
        }

        return self.__calculate_result(outcomes)

    def part_two(self):
        outcomes = {
            'A X': 3,
            'A Y': 4,
            'A Z': 8,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 2,
            'C Y': 6,
            'C Z': 7,
        }

        return self.__calculate_result(outcomes)

    def __calculate_result(self, outcomes, result=0):
        for line in self.input:
            outcome = line.strip('\n')
            result += outcomes[outcome]

        return result
