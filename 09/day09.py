"""
--- Day 9: Supply Stacks  ---
https://adventofcode.com/2022/day/9
"""


def parse_input_file():
    """parse input file"""
    steps = []
    # parse input file
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            splitted_line = line.strip().split()
            direction = splitted_line[0]
            step_size = int(splitted_line[1])
            steps.append((direction, step_size))
    return steps


def parse_step(arg_step):
    """parse step"""
    x_mov = 0
    y_mov = 0
    if arg_step[0] == "R":
        x_mov = 0
        y_mov = 1
    if arg_step[0] == "U":
        x_mov = -1
        y_mov = 0
    if arg_step[0] == "L":
        x_mov = 0
        y_mov = -1
    if arg_step[0] == "D":
        x_mov = 1
        y_mov = 0
    return x_mov, y_mov


def get_visited(arg_steps, arg_size):
    """calculates visited position for fiven size"""
    visited = set()

    positions = []
    for _ in range(arg_size):
        positions.append([15, 11])
    for step in arg_steps:
        x_mov, y_mov = parse_step(step)

        for _ in range(step[1]):
            positions[0][0] += x_mov
            positions[0][1] += y_mov
            for i in range(1, len(positions)):
                delta_x = positions[i-1][0]-positions[i][0]
                delta_y = positions[i-1][1]-positions[i][1]
                if abs(delta_x) > 1 or abs(delta_y) > 1:
                    if delta_x == 0:
                        positions[i][1] += 1 if delta_y > 0 else -1
                    elif delta_y == 0:
                        positions[i][0] += 1 if delta_x > 0 else -1
                    else:
                        positions[i][0] += 1 if delta_x > 0 else -1
                        positions[i][1] += 1 if delta_y > 0 else -1

            # mark tails visited position
            visited.add((positions[-1][0], positions[-1][1]))
    return len(visited)


print("first start-of-packet marker (4):",  get_visited(parse_input_file(), 2))
print("first start-of-packet marker (14):",
      get_visited(parse_input_file(), 10))
