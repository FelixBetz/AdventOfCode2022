"""
--- Day 18: Boiling Boulders  ---
https://adventofcode.com/2022/day/18
"""


class Cube():
    """represents a cube"""

    def __init__(self, arg_x, arg_y, arg_z) -> None:
        self.x = arg_x
        self.y = arg_y
        self.z = arg_z
        self.sides_connected = [False] * 6
        self.__create_sides()
        self.__create_corners()

    def __create_sides(self):
        x = self.x
        y = self.y
        z = self.z
        self.sides = []*6
        # front
        self.sides.append([(x, y, z), (x+1, y, z), (x, y+1, z), (x+1, y+1, z)])
        # back
        self.sides.append([(x, y, z+1), (x+1, y, z+1),
                           (x, y+1, z+1), (x+1, y+1, z+1)])

        # left
        self.sides.append([(x, y, z), (x, y+1, z), (x, y+1, z+1), (x, y, z+1)])
        # right
        self.sides.append([(x+1, y, z), (x+1, y+1, z),
                           (x+1, y+1, z+1), (x+1, y, z+1)])

        # top
        self.sides.append([(x, y+1, z), (x+1, y+1, z),
                           (x, y+1, z+1), (x+1, y+1, z+1)])
        # bot
        self.sides.append([(x, y, z), (x+1, y, z), (x, y, z+1), (x+1, y, z+1)])

    def __create_corners(self):
        front_bot_left = (self.x, self.y, self.z)
        front_bot_right = (self.x+1, self.y, self.z)
        front_top_left = (self.x, self.y+1, self.z)
        front_top_right = (self.x+1, self.y+1, self.z)

        back_bot_left = (self.x, self.y, self.z+1)
        back_bot_right = (self.x+1, self.y, self.z+1)
        back_top_left = (self.x, self.y+1, self.z+1)
        back_top_right = (self.x+1, self.y+1, self.z+1)
        self.corners = [front_bot_left, front_bot_right, front_top_left, front_top_right,
                        back_bot_left, back_bot_right, back_top_left, back_top_right]

    def get_not_connected_sides(self):
        """get amount of not connected sides"""
        ret = 0
        for side in self.sides_connected:
            if not side:
                ret += 1
        return ret

    def mark_sides(self, arg_corners):
        """mark connected sides"""
        for i, side in enumerate(self.sides):
            ret = True
            for corner in arg_corners:
                if corner not in side:
                    ret = False
            if ret:
                self.sides_connected[i] = True

    def __str__(self) -> str:
        return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+") "


def parse_input_file():
    """parse input file"""
    cubes = []
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            coord = line.strip().split(",")
            cubes.append(Cube(int(coord[0]),  int(coord[1]),  int(coord[2])))

    return cubes


def check_connected_sides(arg_cube1, arg_cube2):
    """check if there are some sides connected"""
    intersections = []
    for corner in arg_cube1.corners:
        if corner in arg_cube2.corners:
            intersections.append(corner)
    if len(intersections) == 4:
        arg_cube1.mark_sides(intersections)
        arg_cube2.mark_sides(intersections)


def solve_day18_part1():
    """solve day18 part1"""
    cubes = parse_input_file()

    for i, cube in enumerate(cubes):
        for k in range(i+1, len(cubes)):
            check_connected_sides(cube, cubes[k])

    ret_cnt = 0
    for cube in cubes:
        ret_cnt += cube.get_not_connected_sides()
    return ret_cnt


def solve_day18_part2():
    """solve day18 part2"""
    return 0


print("surface area of your scanned lava droplet:", solve_day18_part1())
print("exterior surface area of your scanned lava droplet:", solve_day18_part2())
