from utils.utils import Utils
import re


class Day7(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        return self.__create_tree().solve_part_one()

    def part_two(self):
        return self.__create_tree().solve_part_two()

    def __create_tree(self):
        current_directory = '/'
        root_node = Node(current_directory)
        current_node = root_node
        tree = Tree(root_node)

        for line in self.input:
            cd = re.match(r"\$ cd", line)
            if cd:
                dirname = cd.string.strip('\n').split('$ cd ')[1]
                if dirname == '/':
                    current_node = root_node
                elif dirname == '..':
                    current_node = current_node.parent
                else:
                    child = Node(dirname, current_node)
                    current_node.add_child(child)
                    current_node = child
            elif line.__contains__('dir '):
                dirname = line[4:].strip('\n')
                child = Node(dirname, current_node)
                current_node.add_child(child)
            elif re.match(r"\d+", line):
                value = int(re.match(r"\d+", line).group())
                current_node.add_file(value)

        return tree

class Tree:
    nodes = {}

    def __init__(self, root):
        self.nodes[root.name] = root

    def solve_part_two(self):
        current_node = self.nodes['/']
        nodes = [current_node]
        condition = current_node.file_size - 40000000
        list_closest = []

        while len(nodes) > 0:
            for child in current_node.children:
                child_node = current_node.children[child]
                if child_node.file_size > condition:
                    list_closest.append(child_node.file_size)
                nodes.append(child_node)
            current_node = nodes.pop()

        return min(list_closest, key=lambda x: abs(x - condition))

    def solve_part_one(self):
        current_node = self.nodes['/']
        nodes = [current_node]
        result = 0

        while len(nodes) > 0:
            for child in current_node.children:
                child_node = current_node.children[child]
                if child_node.file_size <= 100000:
                    result += child_node.file_size
                nodes.append(child_node)
            current_node = nodes.pop()

        return result


class Node:
    name = ''
    parent = None
    children = {}
    file_size = 0

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.file_size = 0

    def add_file(self, file):
        self.file_size += file
        while self.has_parent():
            self = self.parent
            self.file_size += file

    def add_child(self, child):
        self.children[child.name] = child

    def has_parent(self):
        return self.parent is not None
