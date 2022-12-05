"""
--- Day 5: Supply Stacks  ---
https://adventofcode.com/2022/day/5
"""


def parse_stacks(arg_stack_str):
    """parses stacks from string array"""
    stacks = []
    num_stacks = len(arg_stack_str[-1].strip().split("   "))
    for i in range(num_stacks):
        stacks.append([])

    for line in arg_stack_str[:-1]:
        index = 1
        for i in range(num_stacks):
            col = line[index:index+1]
            if col != " ":
                stacks[i].append(col)
            index += 4

    for stack in stacks:
        stack.reverse()
    return stacks


def parse_moves(arg_move_str):
    """parses move from string array"""
    moves = []
    for move in arg_move_str:
        if "move" in move:
            move = move.replace("move", "")
            split_from = move.split("from")
            split_to = split_from[1].split("to")

            amount = int(split_from[0].strip())
            move_from = int(split_to[0].strip())
            move_to = int(split_to[1].strip())
            moves.append((amount, move_from, move_to))

    return moves


def solve_day5_part1():
    """solve day5 part1"""
    stack_str = []
    move_str = []
    is_stack = True
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            if line.strip() == "":
                is_stack = False
            if is_stack:
                stack_str.append(line)
            else:
                move_str.append(line)
    stacks = parse_stacks(stack_str)
    moves = parse_moves(move_str)
    for move in moves:
        for _ in range(move[0]):
            item = stacks[move[1]-1].pop()
            stacks[move[2]-1].append(item)

    ret_str = ""
    for stack in stacks:
        ret_str += stack[-1]
    return ret_str


def solve_day5_part2():
    """solve day5 part2"""
    stack_str = []
    move_str = []
    is_stack = True
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            if line.strip() == "":
                is_stack = False
            if is_stack:
                stack_str.append(line)
            else:
                move_str.append(line)
    stacks = parse_stacks(stack_str)
    moves = parse_moves(move_str)

    for move in moves:
        items = []
        for _ in range(move[0]):
            item = stacks[move[1]-1].pop()
            items.append(item)
        if len(items) > 0:
            items.reverse()
        stacks[move[2]-1] += items

    ret_str = ""
    for stack in stacks:
        ret_str += stack[-1]
    return ret_str


print("After the rearrangement procedure completes, what crate ends up on top of each stack:",
      solve_day5_part1())
print("After the rearrangement procedure completes, what crate ends up on top of each stack:",
      solve_day5_part2())
