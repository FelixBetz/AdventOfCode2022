"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/3
"""


def parse_sections_from_string(arg_string):
    """parse elf sections from string"""
    splitted = arg_string.split("-")
    return (int(splitted[0]), int(splitted[1]))


def fully_contains(elf1, elf2):
    """heck if elf1 fully contains the sections of elf2"""
    return elf1[0] >= elf2[0] and elf1[1] <= elf2[1]


def is_overlap(elf1, elf2):
    """check if the sections of two elf overlaps"""
    if elf2[0] <= elf1[0] <= elf2[1]:
        return True
    if elf2[0] <= elf1[1] <= elf2[1]:
        return True

    if elf1[0] <= elf2[0] <= elf1[1]:
        return True
    if elf1[0] <= elf2[1] <= elf1[1]:
        return True

    return False


def solve_day4_part1():
    """solve day3"""
    with open("input.txt", encoding="utf-8") as input_file:
        sum_fully_contains = 0
        for line in input_file:
            splitted = line.strip().split(",")
            first_elf = parse_sections_from_string(splitted[0])
            seconde_elf = parse_sections_from_string(splitted[1])
            if fully_contains(first_elf, seconde_elf) or fully_contains(seconde_elf, first_elf):
                sum_fully_contains += 1
    return sum_fully_contains


def solve_day4_part2():
    """solve day3"""
    with open("input.txt", encoding="utf-8") as input_file:
        overlaps = 0
        for line in input_file:
            splitted = line.strip().split(",")
            first_elf = parse_sections_from_string(splitted[0])
            seconde_elf = parse_sections_from_string(splitted[1])
            if is_overlap(first_elf, seconde_elf):
                overlaps += 1

    return overlaps


print("assignment pairs does one range fully contain the other:", solve_day4_part1())
print("assignment pairs do the ranges overlap:", solve_day4_part2())
