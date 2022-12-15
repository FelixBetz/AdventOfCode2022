"""
--- Day 13: Distress Signal  ---
https://adventofcode.com/2022/day/13
"""

from functools import cmp_to_key
import json


def parse_input_file():
    """parse input file"""
    packets = []
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.strip()
            if line != "":
                packets.append(json.loads(line))
    return packets


def is_int(arg_num):
    """check if given item is of type int"""
    return isinstance(arg_num, int)


def is_list(arg_list):
    """check if given item is of type list"""
    return isinstance(arg_list, list)


def compare_ints(arg_a, arg_b):
    """compare two ints"""
    if arg_a > arg_b:
        return 1
    if arg_b > arg_a:
        return -1
    return 0


def compare(arg_a, arg_b):
    """copare two items"""
    # int vs int
    if is_int(arg_a) and is_int(arg_b):
        return compare_ints(arg_a, arg_b)
        # list vs int
    if is_list(arg_a) and is_list(arg_b):
        min_lenght = min(len(arg_a), len(arg_b))
        for i in range(min_lenght):
            ret = compare(arg_a[i], arg_b[i])
            if ret != 0:
                return ret
        if len(arg_a) > len(arg_b):
            return 1
        if len(arg_b) > len(arg_a):
            return -1
        return 0

    if is_int(arg_a):
        arg_a = [arg_a]
    elif is_int(arg_b):
        arg_b = [arg_b]
    return compare(arg_a, arg_b)


def solve_day13_part1():
    """solve day13 part1"""
    packets = parse_input_file()

    ret_sum = []
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i+1]) < 0:
            ret_sum.append((i//2) + 1)

    return sum(ret_sum)


def solve_day13_part2():
    """solve day13 part2"""
    packets = parse_input_file()

    # add additional divider packets
    divider_packets = [[[2]]], [[6]]
    packets += divider_packets

    packets = sorted(packets, key=cmp_to_key(compare), reverse=False)

    decoder_key = 1
    for packet in divider_packets:
        decoder_key *= 1 + packets.index(packet)

    return decoder_key


print("sum of the indices of those pairs:", solve_day13_part1())
print("What is the decoder key for the distress signal:", solve_day13_part2())
