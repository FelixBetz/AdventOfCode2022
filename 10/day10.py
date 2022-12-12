"""
--- Day 10: Supply Stacks  ---
https://adventofcode.com/2022/day/10
"""


def solve_day10_part1():
    """solve day10 part1"""

    reg_x = 1
    cycle = 1
    ssi = 0
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.strip()
            cmds = []
            if "noop" in line:
                cmds.append(0)
            elif "addx" in line:
                num = int(line.split(" ")[1])
                cmds.append(0)
                cmds.append(num)

            for cmd in cmds:
                reg_x += cmd
                cycle += 1
                if (cycle - 20) % 40 == 0 and cycle <= 220:
                    ssi += cycle * reg_x

    return ssi


def array_rotate(arr, reverse):
    """rotate array"""
    if reverse:
        arr[:] = arr[1:]+arr[0:1]
    else:
        arr[:] = arr[-1:]+arr[0:-1]
    return arr


def solve_day10_part2():
    """solve day10 part2"""
    cmds = []
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.strip()
            if "noop" in line:
                cmds.append(0)
            elif "addx" in line:
                num = int(line.split(" ")[1])
                cmds.append(0)
                cmds.append(num)

    print("len", len(cmds))
    cycle = 0

    sprite = "###....................................."
    sprite = list(sprite)
    current_row = []
    display = []
    for cmd in cmds:
        cycle += 1
        if len(current_row) == 40:
            display.append(current_row)
            current_row = []

        current_row.append(sprite[(cycle - 1) % 40])
        if cmd != 0:
            for _ in range(0, abs(cmd)):
                if cmd > 0:
                    sprite = array_rotate(sprite, False)
                else:
                    sprite = array_rotate(sprite, True)
    display.append(current_row)
    for row in display:
        print(" ".join(row).replace(".", " "))


print("sum of these six signal strengths:", solve_day10_part1())
solve_day10_part2()
