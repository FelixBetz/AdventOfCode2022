"""
--- Day 6: Supply Stacks  ---
https://adventofcode.com/2022/day/6
"""


def get_distinc_cnt(arg_data, arg_distinc):
    """get_distinc_cnts"""
    cnt_chars = arg_distinc-1
    stream = []
    for i in range(arg_distinc-1):
        stream.append(arg_data[i])
    for char in arg_data[arg_distinc-1:]:
        stream.append(char)
        cnt_chars += 1
        is_four = True
        for elem in stream:
            if stream.count(elem) > 1:
                is_four = False
                break
        if is_four:
            break
        stream = stream[1:]
    return cnt_chars


def solve_day6_part1():
    """solve day6 part1"""
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            return get_distinc_cnt(line, 4)


def solve_day6_part2():
    """solve day6 part1"""
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            return get_distinc_cnt(line, 14)


print("first start-of-packet marker (4):", solve_day6_part1())
print("first start-of-packet marker (14):", solve_day6_part2())
