from utils.utils import Utils


class Day1(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        result = 0
        max_result = 0
        for line in self.input:
            if line != '\n':
                result += int(line)
            else:
                max_result = result if result > max_result else max_result
                result = 0
        return max_result

    def part_two(self):
        results = []
        result = 0
        for line in self.input:
            if line != '\n':
                result += int(line)
            else:
                results.append(result)
                result = 0

        return sum(sorted(results, reverse=True)[:3])


day1 = Day1()
print(day1.part_one())
print(day1.part_two())
