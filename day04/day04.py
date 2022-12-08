from utils.utils import Utils


class Day4(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        result = 0
        for line in self.input:
            arr = self.__convert_to_array(line)

            if arr[0] <= arr[2] and arr[1] >= arr[3]:
                result += 1

            elif arr[2] <= arr[0] and arr[3] >= arr[1]:
                result += 1

        return result

    def part_two(self):
        result = 0
        for line in self.input:
            arr = self.__convert_to_array(line)

            if arr[1] >= arr[2] and arr[3] >= arr[0]:
                result += 1

        return result

    def __convert_to_array(self, line):
        arr = []
        pairs = line.strip('\n').split(',')
        for pair in pairs:
            arr.append(list(map(int, pair.split('-'))))

        return self.flatten(arr)

