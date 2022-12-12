"""
--- Day 11: Monkey in the Middle  ---
https://adventofcode.com/2022/day/11
"""


import math


class Moneky:
    """represents a monkey"""

    def __init__(self, arg_num, arg_items, arg_operation, arg_divisible_by, arg_true, arg_false):
        self.num = arg_num
        self.items = arg_items
        self.operation = arg_operation
        self.divisible_by = arg_divisible_by
        self.if_true = arg_true
        self.if_false = arg_false
        self.inspected = 0

    def execute_operation(self, lcm=None):
        """execute operation on monkey"""
        ret = []
        for i, item in enumerate(self.items):
            self.inspected += 1

            if "old" in self.operation[2]:
                second_operator = item
            else:
                second_operator = int(self.operation[2])

            if self.operation[1] == "+":
                self.items[i] += second_operator
            elif self.operation[1] == "*":
                self.items[i] *= second_operator
            if lcm is None:
                ret_item = self.items[i] // 3
            else:
                ret_item = self.items[i] % lcm

            if ret_item % self.divisible_by == 0:
                ret.append((self.if_true, ret_item))
            else:
                ret.append((self.if_false, ret_item))
        self.items = []
        return ret

    def __repr__(self) -> str:
        ret_str = "Monkey "+str(self.num)+": "
        ret_str += str(self.items)
        ret_str += "\t("+str(self.inspected)+")"

        return ret_str.replace("[", "").replace("]", "")


def parse_monkeys():
    """parses monkey from input file"""
    lines = []

    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            lines.append(line.strip())

    monkeys = []
    for i in range(0, len(lines), 7):
        # 0: monkey
        num = int(lines[i].split()[1].replace(":", ""))

        # 1: items
        items_str = lines[i+1].split(":")[1].split(",")
        items = []
        for item in items_str:
            items.append(int(item.strip()))

        # 2: operation
        operation = lines[i+2].split("=")[1].strip().split(" ")

        # 3 test name
        divisible_by = int(lines[i+3].split("by")[1].strip())

        # 4 if true
        if_true_throw = int(lines[i+4].split("monkey")[1].strip())
        # 5 if false
        if_false_throw = int(lines[i+5].split("monkey")[1].strip())
        monkeys.append(Moneky(num, items, operation,
                       divisible_by, if_true_throw, if_false_throw))
    return monkeys


def solve_day11_part1():
    """solve day11 part1"""
    monkeys = parse_monkeys()
    for _ in range(20):
        for monkey in monkeys:
            rets = monkey.execute_operation()
            for ret in rets:
                monkeys[ret[0]].items.append(ret[1])
    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort(reverse=True)

    return inspected[0] * inspected[1]


def solve_day11_part2():
    """solve day11 part2"""
    monkeys = parse_monkeys()
    lcm = math.lcm(*[monkey.divisible_by for monkey in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            rets = monkey.execute_operation(lcm=lcm)
            for ret in rets:
                monkeys[ret[0]].items.append(ret[1])

    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort(reverse=True)

    return inspected[0] * inspected[1]


print("monkey business after 20 rounds:", solve_day11_part1())
print("monkey business after 10000 rounds:", solve_day11_part2())
