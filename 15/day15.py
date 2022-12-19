"""
--- Day 15: Beacon Exclusion Zone  ---
https://adventofcode.com/2022/day/15
"""


class Sensor():
    """represents a sensor"""

    def __init__(self, arg_x, arg_y, arg_beacon_x, arg_beacon_y) -> None:
        self.pos_x = arg_x
        self.pos_y = arg_y
        self.beacon_x = arg_beacon_x
        self.beacon_y = arg_beacon_y

    def get_pos_string(self):
        """ returns position string"""
        return "("+str(self.pos_x) + "|"+str(self.pos_y) + "): "

    def get_beacon_string(self):
        """returns beacon string"""
        return "("+str(self.beacon_x) + "|"+str(self.beacon_y) + "): "

    def __repr__(self) -> str:
        ret_str = self.get_pos_string() + ": "
        ret_str += "beacon pos "+self.get_beacon_string()
        return ret_str


def parse_input_file():
    """parse input file"""
    sensors = []
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            splitted_line = line.strip().split(":")

            sensor_splitted = splitted_line[0]\
                .replace("Sensor at ", "")\
                .replace("x=", "")\
                .replace("y=", "")\
                .split(",")

            beacon_splitted = splitted_line[1]\
                .replace("closest beacon is at ", "")\
                .replace("x=", "")\
                .replace("y=", "")\
                .split(",")

            sensor = Sensor(int(sensor_splitted[0]), int(sensor_splitted[1]), int(
                beacon_splitted[0]), int(beacon_splitted[1]))
            sensors.append(sensor)
    return sensors


def cannot_containbeacon_positions(arg_sensors, arg_compare_index):
    """cannot_containbeacon_positions"""

    sensor_set = set()
    beacon_set = set()

    for sensor in arg_sensors:
        # calc https://en.wikipedia.org/wiki/Taxicab_geometry:
        dist = abs(sensor.beacon_y-sensor.pos_y) + \
            abs(sensor.beacon_x-sensor.pos_x)

        for row_offset in range(-dist, 1 + dist):
            if sensor.beacon_y == arg_compare_index:
                beacon_set.add(sensor.beacon_x)
            # skip row if, row index does not match compare index
            if row_offset + sensor.pos_y != arg_compare_index:
                continue

            # calc height
            height = row_offset % dist
            if row_offset > 0:
                height = (dist - row_offset) % dist

            for col_offset in range(-dist, 1 + dist):
                if height >= abs(col_offset) and sensor.pos_y+row_offset == arg_compare_index:
                    sensor_set.add(sensor.pos_x+col_offset)

    ret_cnt = len(list(sensor_set))
    # remove positions, that are mark as beacon
    for beacon in beacon_set:
        if beacon in beacon_set:
            ret_cnt -= 1

    return ret_cnt


def solve_day15_part1():
    """solve day15 part1"""
    sensors = parse_input_file()

    return cannot_containbeacon_positions(sensors, 2000000)


def solve_day15_part2():
    """solve day15 part2"""
    sensors = parse_input_file()
    return 0


print("how many positions cannot contain a beacon:", solve_day15_part1())
print("What is the decoder key for the distress signal:", solve_day15_part2())
