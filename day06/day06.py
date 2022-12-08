from utils.utils import Utils, Day


class Day6(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        return self.__get_solution(Day.part_one)

    def part_two(self):
        return self.__get_solution(Day.part_two)

    def __get_solution(self, part):
        match part:
            case Day.part_one:
                counter = 4
            case Day.part_two:
                counter = 14

        step = counter

        for line in self.input:
            while len(set(line[counter - step:counter])) != len(line[counter - step:counter]):
                counter += 1

        return counter



