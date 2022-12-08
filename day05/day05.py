from utils.utils import Utils, DayPart
import re


class Day5(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        crates = {}

        for line in self.input:
            crates = self.__split_to_columns(line, crates)
            crates = self.__move_crates(line, crates, DayPart.part_one)

        return self.__get_result(crates)

    def part_two(self):
        crates = {}

        for line in self.input:
            crates = self.__split_to_columns(line, crates)
            crates = self.__move_crates(line, crates, DayPart.part_two)

        return self.__get_result(crates)

    def __split_to_columns(self, line, crates):
        split = line.strip('\n').split(' ')
        column_counter = 1
        if line.__contains__('['):
            while len(split) > 0:
                if split[0] != '':
                    if column_counter not in crates:
                        crates[column_counter] = []
                    crates[column_counter].append(split.pop(0).strip('[]'))
                else:
                    split = split[4:]

                column_counter += 1

        return crates

    def __move_crates(self, line, crates, part):
        if line.__contains__('move'):
            command = list(map(int, re.findall(r"\d+", line)))
            quantity = command[0]
            column_from = command[1]
            column_to = command[2]

            if part == DayPart.part_one:
                for _ in range(0, quantity):
                    crate_to_move = crates[column_from].pop(0)
                    crates[column_to].insert(0, crate_to_move)
            else:
                crates[column_to] = crates[column_from][0:quantity] + crates[column_to]
                del crates[column_from][0:quantity]

        return crates

    def __get_result(self, crates):
        result = ''

        for i in range(1, len(crates) + 1):
            result += crates[i][0]

        return result

