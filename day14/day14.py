from utils.utils import Utils


class Day14(Utils):
    grid: set
    ymax: int

    def __init__(self):
        super().__init__()

    def part_one(self):
        self.grid = self.create_grid()
        sorted_by_y = sorted(self.grid, key=lambda tup: tup[1], reverse=True)
        self.ymax = sorted_by_y[0][1] - 1

        sand = (500, 0)
        rock_size = len(self.grid)
        while self.add_sand(sand):
            pass

        return len(self.grid) - 1 - rock_size

    def part_two(self):
        self.grid = self.create_grid()
        sorted_by_y = sorted(self.grid, key=lambda tup: tup[1], reverse=True)
        self.ymax = sorted_by_y[0][1]

        sand = (500, 0)
        rock_size = len(self.grid)
        while sand not in self.grid:
            self.add_sand(sand)

        return len(self.grid) - rock_size

    def add_sand(self, sand):
        x = sand[0]
        y = sand[1]

        if y > self.ymax:
            self.grid.add(sand)
            return False
        elif (x, y + 1) not in self.grid:
            return self.add_sand((x, y + 1))
        elif (x - 1, y + 1) not in self.grid:
            return self.add_sand((x - 1, y + 1))
        elif (x + 1, y + 1) not in self.grid:
            return self.add_sand((x + 1, y + 1))
        else:
            self.grid.add(sand)

        return True

    def create_grid(self):
        endpoints = set()

        for line in self.input:
            points = []
            coords = line.strip().split(' -> ')
            for coord in coords:
                xy = coord.split(',')
                point = (int(xy[0]), int(xy[1]))
                points.append(point)
            for i in range(1, len(points)):
                point1 = points[i - 1]
                point2 = points[i]

                if point1[0] == point2[0]:
                    if point1[1] > point2[1]:
                        start = point2[1]
                        end = point1[1] + 1
                    else:
                        start = point1[1]
                        end = point2[1] + 1

                    for y in range(start, end):
                        endpoints.add((point1[0], y))
                else:
                    if point1[0] > point2[0]:
                        start = point2[0]
                        end = point1[0] + 1
                    else:
                        start = point1[0]
                        end = point2[0] + 1

                    for x in range(start, end):
                        endpoints.add((x, point1[1]))

        return endpoints
