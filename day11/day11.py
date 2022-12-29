from utils.utils import Utils
import re


class Day11(Utils):

    def __init__(self):
        super().__init__()

    def part_one(self):
        monkeys = self.__setup_monkeys()
        monkey_standings = dict()

        for monkey in monkeys:
            monkey_standings[monkey.id] = monkey.starting_items

        for _ in range(20):
            for monkey in monkeys:
                for item in monkey_standings[monkey.id]:
                    item = monkey.operation_eval(item)
                    item //= 3
                    monkey.inspected += 1
                    if item % monkey.divider == 0:
                        monkey_standings[monkey.true].append(item)
                    else:
                        monkey_standings[monkey.false].append(item)
                    monkey_standings[monkey.id] = []

        result = sorted(monkeys, key=lambda x: x.inspected, reverse=True)

        return result[0].inspected * result[1].inspected

    def part_two(self):
        monkeys = self.__setup_monkeys()
        monkey_standings = dict()
        mod = 1

        for monkey in monkeys:
            monkey_standings[monkey.id] = monkey.starting_items
            mod *= monkey.divider

        for i in range(10000):
            for monkey in monkeys:
                for item in monkey_standings[monkey.id]:
                    item = monkey.operation_eval(item)
                    item %= mod
                    monkey.inspected += 1
                    if item % monkey.divider == 0:
                        monkey_standings[monkey.true].append(item)
                    else:
                        monkey_standings[monkey.false].append(item)
                    monkey_standings[monkey.id] = []

        result = sorted(monkeys, key=lambda x: x.inspected, reverse=True)

        return result[0].inspected * result[1].inspected

    def __setup_monkeys(self):
        monkey = None
        monkeys = []
        for line in self.input:
            strip = line.strip()
            if strip.startswith('Monkey'):
                monkey = Monkey()
                monkey.id = int(re.findall(r"\d+", strip)[0])
                monkey.inspected = 0
            elif strip.startswith('Starting items:'):
                monkey.starting_items = list(map(int, re.findall(r"\d+", strip)))
            elif strip.startswith('Operation:'):
                monkey.operation = strip
                monkey.set_operation()
            elif strip.startswith('Test:'):
                monkey.test = strip
                monkey.set_divider()
            elif strip.startswith('If true:'):
                monkey.true_statement = strip
                monkey.set_true()
            elif strip.startswith('If false:'):
                monkey.false_statement = strip
                monkey.set_false()
                monkeys.append(monkey)

        return monkeys


class Monkey:
    id: int
    starting_items: []
    operation: str
    test: str
    true_statement: str
    false_statement: str
    inspected: int
    divider: int
    true: int
    false: int
    operation_eval: None

    def set_divider(self):
        divider = int(re.findall(r"\d+", self.test)[0])
        self.divider = divider

    def set_true(self):
        result = int(re.findall(r"\d+", self.true_statement)[0])
        self.true = result

    def set_false(self):
        result = int(re.findall(r"\d+", self.false_statement)[0])
        self.false = result

    def set_operation(self):
        op = re.split(r"= ", self.operation)
        self.operation_eval = eval("lambda old:" + op[1])

    def __str__(self):
        return str(self.inspected)
