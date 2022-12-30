from utils.utils import Utils
from collections import deque


class Day12(Utils):
    graph: list

    def __init__(self):
        super().__init__()

    def part_one(self):
        self.graph = [list(line.strip()) for line in self.input]
        start, end = self.__setup_graph()

        return self.__bfs_part_one(start, end)

    def part_two(self):
        self.graph = [list(line.strip()) for line in self.input]
        start, end = self.__setup_graph()

        return self.__bfs_part_two(end)

    def __setup_graph(self, start=None, end=None):
        for row, line in enumerate(self.graph):
            if 'S' in line:
                column = line.index('S')
                start = (row, column)
                self.graph[row][column] = "a"
            if 'E' in line:
                column = line.index('E')
                end = (row, column)
                self.graph[row][column] = "z"

        return start, end

    def __bfs_part_one(self, start, end):
        queue = deque()
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_limit = len(self.graph)
        column_limit = len(self.graph[0])

        queue.append([start])

        while queue:
            node = queue.popleft()
            row, column = node[-1]
            if (row, column) not in visited:
                visited.add((row, column))
                if (row, column) == end:
                    return len(node) - 1

                ch_original = self.graph[row][column]
                for d_row, d_column in directions:
                    neighbour = (row + d_row, column + d_column)
                    if 0 <= neighbour[0] < row_limit and 0 <= neighbour[1] < column_limit:
                        ch = self.graph[neighbour[0]][neighbour[1]]
                        if ord(ch) <= ord(ch_original) + 1:
                            node_copy = node[:]
                            node_copy.append(neighbour)
                            queue.append(node_copy)

    def __bfs_part_two(self, start):
        queue = deque()
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_limit = len(self.graph)
        column_limit = len(self.graph[0])

        queue.append([start])

        while queue:
            node = queue.popleft()
            row, column = node[-1]
            if (row, column) not in visited:
                visited.add((row, column))
                ch_original = self.graph[row][column]
                if ch_original == 'a':
                    return len(node) - 1
                for d_row, d_column in directions:
                    neighbour = (row + d_row, column + d_column)
                    if 0 <= neighbour[0] < row_limit and 0 <= neighbour[1] < column_limit:
                        ch = self.graph[neighbour[0]][neighbour[1]]
                        if ord(ch) - ord(ch_original) >= -1:
                            node_copy = node[:]
                            node_copy.append(neighbour)
                            queue.append(node_copy)
