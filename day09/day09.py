from utils.utils import Utils


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Day9(Utils):
    head: Point
    tail: Point

    def __init__(self):
        super().__init__()

    def part_one(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        visited = {(0, 0)}

        for line in self.input:
            direction, step = line.split()
            step = int(step)

            for _ in range(step):
                diff = self.__calc_diff(direction)
                self.__calc_tail(diff, self.tail)
                visited.add(tuple([self.tail.x, self.tail.y]))

        return len(visited)

    def part_two(self):
        visited = {(0, 0)}

        motions = [Point(0, 0) for _ in range(10)]

        for line in self.input:
            direction, step = line.split()
            step = int(step)

            for _ in range(step):
                self.__calc_diff(direction, motions)
                for i in range(9):
                    head = motions[i]
                    tail = motions[i + 1]

                    diff = Point(head.x - tail.x, head.y - tail.y)

                    self.__calc_tail(diff, tail)

                    visited.add(tuple([motions[-1].x, motions[-1].y]))

        return len(visited)

    def __calc_diff(self, direction, motions=None):
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0

        if motions is not None:
            motions[0].x += dx
            motions[0].y += dy
        else:
            self.head.x += dx
            self.head.y += dy

            return Point(self.head.x - self.tail.x, self.head.y - self.tail.y)

    def __calc_tail(self, diff, tail):
        if abs(diff.x) > 1 or abs(diff.y) > 1:
            if diff.x == 0:
                tail.y += diff.y // 2
            elif diff.y == 0:
                tail.x += diff.x // 2
            else:
                tail.x += 1 if diff.x > 0 else -1
                tail.y += 1 if diff.y > 0 else -1
