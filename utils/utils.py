from abc import ABCMeta, abstractmethod
from enum import Enum
import os
import re


class Utils(object, metaclass=ABCMeta):
    _input = None
    _custom_input = None

    @abstractmethod
    def __init__(self):
        filepath = os.path.abspath('input.txt')
        if not os.path.isfile(filepath):
            raise Exception("Path to the file is incorrect, make sure you name the input file as input.txt")

        file = open(filepath)
        self.input = file.readlines()
        file.close()

        if re.search('tests/', filepath):
            filepath = re.sub('tests/', '', os.path.abspath('input.txt'))
            file = open(filepath)
            self.custom_input = file.readlines()
            file.close()

    def flatten(self, list_to_flatten):
        return [item for sublist in list_to_flatten for item in sublist]


class GridCreator:
    grid = [[]]
    __input_file = None
    __max_col = 0
    __max_row = 0

    def __init__(self, input_file):
        self.__input_file = input_file
        self._create_grid()

    def _create_grid(self):
        self.grid = [list(map(int, line.strip('\n'))) for line in self.__input_file]
        self.__max_row = len(self.grid)
        self.__max_col = len(self.grid[self.__max_row - 1])

        for row in range(self.__max_row):
            for col in range(self.__max_col):
                value = self.grid[row][col]
                point = Point(value, col, row)
                self.grid[row][col] = point

        for row in range(self.__max_row):
            for col in range(self.__max_col):
                point = self.grid[row][col]
                self.__set_right(point)
                self.__set_left(point)
                self.__set_top(point)
                self.__set_bottom(point)

    def __set_right(self, point):
        if point.column_key < self.__max_col - 1:
            point.set_right(self.grid[point.row_key][point.column_key + 1])

    def __set_left(self, point):
        if point.column_key != 0:
            point.set_left(self.grid[point.row_key][point.column_key - 1])

    def __set_top(self, point):
        if point.row_key != 0:
            point.set_top(self.grid[point.row_key - 1][point.column_key])

    def __set_bottom(self, point):
        if point.row_key < self.__max_row - 1:
            point.set_bottom(self.grid[point.row_key + 1][point.column_key])


class Point:
    value = None
    column_key = None
    row_key = None
    right = None
    left = None
    top = None
    bottom = None

    def __init__(self, value, column_key, row_key):
        self.value = value
        self.column_key = column_key
        self.row_key = row_key

    def has_right(self):
        return self.right is not None

    def has_left(self):
        return self.left is not None

    def has_top(self):
        return self.top is not None

    def has_bottom(self):
        return self.bottom is not None

    def set_right(self, point):
        self.right = point

    def set_left(self, point):
        self.left = point

    def set_top(self, point):
        self.top = point

    def set_bottom(self, point):
        self.bottom = point

    def __str__(self):
        return 'Value: {}\nCol: {}\nRow: {}\nTop: {}\nRight: {}\nBottom: {}\nLeft: {}\n'\
            .format(self.value, self.column_key, self.row_key, self.top, self.right, self.bottom, self.left)


class Day(Enum):
    part_one = 1
    part_two = 2
