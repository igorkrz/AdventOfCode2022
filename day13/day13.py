from utils.utils import Utils


class Day13(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        packets = [eval(line.strip()) for line in self.input if line != '\n']
        result = 0

        for i in range(1, len(packets), 2):
            packet1 = packets[i - 1]
            packet2 = packets[i]

            if self.compare_packets(packet1, packet2) < 0:
                result += (i + 1) // 2

        return result

    def part_two(self):
        packets = [eval(line.strip()) for line in self.input if line != '\n']
        packet2 = 1
        packet6 = 2

        for i in range(len(packets)):
            packet = packets[i]
            if self.compare_packets(packet, [[2]]) < 0:
                packet2 += 1
                packet6 += 1
            elif self.compare_packets(packet, [[6]]) < 0:
                packet6 += 1

        return packet2 * packet6

    def compare_packets(self, arr1, arr2):
        if type(arr1) == int:
            if type(arr2) == int:
                return arr1 - arr2
            else:
                return self.compare_packets([arr1], arr2)
        else:
            if type(arr2) == int:
                return self.compare_packets(arr1, [arr2])
            else:
                for a, b in zip(arr1, arr2):
                    result = self.compare_packets(a, b)
                    if result:
                        return result

        return len(arr1) - len(arr2)
