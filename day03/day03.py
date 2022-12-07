from utils.utils import Utils


class Day3(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        result = 0

        for line in self.input:
            string1, string2 = set(line[:len(line) // 2].strip('\n')), set(line[len(line) // 2:].strip('\n'))
            intersection = string1 & string2

            result += self.__calculate_result(intersection)

        return result

    def part_two(self):
        result = 0
        group = []

        for line in self.input:
            string = set(line.strip('\n'))
            group.append(string)

            if len(group) == 3:
                string1, string2, string3 = group.pop(), group.pop(), group.pop()

                intersection1 = string1 & string2
                intersection2 = string2 & string3
                intersection = intersection1 & intersection2

                result += self.__calculate_result(intersection)

        return result

    def __calculate_result(self, intersection):
        ascii_letter = ord(intersection.pop())

        if ascii_letter > 96:
            result = ascii_letter - 96
        else:
            result = ascii_letter - 38

        return result
