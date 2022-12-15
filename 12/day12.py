"""
--- Day 12: Monkey in the Middle  ---
https://adventofcode.com/2022/day/12
"""


class Point():
    """represents a Point"""

    def __init__(self, arg_x, arg_y):
        self.pos_x = arg_x
        self.pos_y = arg_y
        self.height = 0

    def __repr__(self) -> str:
        return "("+str(self.pos_x)+"|"+str(self.pos_y)+"): "+str(self.height)

    def get_point_as_tuple(self):
        """returns point as tuple"""
        return (self.pos_x, self.pos_y)


def parse_input_file():
    """parses input file"""
    heightmap = []
    with open("input.txt", encoding="utf-8") as input_file:

        for i, line in enumerate(input_file):
            row = []
            for k, char in enumerate(line.strip()):
                point = Point(i, k)
                if char == "S":
                    char = "a"
                    pos = point
                elif char == "E":
                    char = "z"
                    end_pos = point
                point.height = ord(char)-ord("a")+1
                row.append(point)
            heightmap.append(row)
    return heightmap, pos, end_pos


def is_in_grid(arg_heightmap, arg_point, arg_max_x, arg_max_y) -> bool:
    """ Check if a location is within the grid """
    if (0 <= arg_point[0] < arg_max_x and 0 <= arg_point[1] < arg_max_y):
        return arg_heightmap[arg_point[0]][arg_point[1]]

    return None


def get_neighbours(arg_heightmap, arg_point, arg_max_x, arg_max_y):
    """ Return all adjacent orthogonal (not diagonal) Points """

    neighbours = [(arg_point.pos_x+dx, arg_point.pos_y+dy) for dx in range(-1, 2)
                  for dy in range(-1, 2)
                  if abs(dy) != abs(dx)]
    filterd_neighbours = []

    for neighbour in neighbours:
        ret = is_in_grid(
            arg_heightmap, (neighbour[0], neighbour[1]), arg_max_x, arg_max_y)
        if ret is not None:
            if arg_point.height + 1 >= ret.height:
                filterd_neighbours.append(ret)

    return filterd_neighbours


def bfs(arg_heightmap, arg_visited, arg_start_pos, arg_end_pos):
    """bfs"""
    arg_visited.append(arg_start_pos)
    queue = [arg_start_pos]

    came_from = {}
    came_from[arg_start_pos] = None
    while queue:
        current_pos = queue.pop(0)
        if current_pos == arg_end_pos:
            break

        neighbours = get_neighbours(arg_heightmap, current_pos, len(
            arg_heightmap), len(arg_heightmap[0]))

        for neighbour in neighbours:
            if neighbour not in arg_visited:
                arg_visited.append(neighbour)
                queue.append(neighbour)
                came_from[neighbour] = current_pos
            # build the breadcrumb path

    if current_pos != arg_end_pos:
        return None  # No valid path from this point

    current = arg_end_pos
    path = []
    while current != arg_start_pos:
        path.append(current)
        current = came_from[current]

    return len(path)


def solve_day12_part1():
    """solve day11 part1"""
    # print(pos, end_pos)
    heightmap, pos, end_pos, = parse_input_file()
    return bfs(heightmap, [], pos, end_pos)


def solve_day12_part2():
    """solve day11 part2"""
    heightmap, pos, end_pos, = parse_input_file()
    min_length = len(heightmap[0]) * len(heightmap)
    for row in heightmap:
        for point in row:
            if point.height == 1:
                ret = bfs(heightmap, [], point, end_pos)
                if ret is not None:
                    min_length = min(min_length, ret)
    return min_length


print("monkey business after 20 rounds:", solve_day12_part1())
print("monkey business after 10000 rounds:", solve_day12_part2())
