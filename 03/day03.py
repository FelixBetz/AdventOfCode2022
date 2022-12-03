"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
"""


def get_item_priority(item):
    """get priorty of the item"""
    if item.isupper():
        return ord(item) - ord("A") + 1+26
    return ord(item) - ord("a") + 1


def solve_day3_part1():
    """solve day3"""
    with open("input.txt", encoding="utf-8") as input_file:
        sum_priorities = 0
        for line in input_file:
            line = line.strip()
            first = line[:len(line)//2]
            second = line[len(line)//2:]
            for item in first:
                if item in second:
                    sum_priorities += get_item_priority(item)
                    break
    return sum_priorities


def solve_day3_part2():
    """solve day3"""
    with open("input.txt", encoding="utf-8") as input_file:
        sum_priorities = 0
        rucksacks = []
        for line in input_file:
            rucksacks.append(line.strip())

        for i in range(0, len(rucksacks), 3):
            for item in rucksacks[i]:
                if item in list(rucksacks[i+1]) and item in list(rucksacks[i+2]):
                    sum_priorities += get_item_priority(item)
                    break

    return sum_priorities


print("sum of the priorities of those item types:", solve_day3_part1())
print("sum of the priorities of those item types:", solve_day3_part2())
