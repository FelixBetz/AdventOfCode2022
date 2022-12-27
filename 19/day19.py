"""
--- Day 19: Not Enough Minerals  ---
https://adventofcode.com/2022/day/19
"""
from dataclasses import dataclass
from collections import deque


class Blueprint:
    """represents Blueprint"""

    def __init__(self, arg_id, arg_ore, arg_clay, arg_obsidian, arg_geode) -> None:
        self.num = arg_id
        self.ore = arg_ore
        self.clay = arg_clay
        self.obsidian = arg_obsidian
        self.geode = arg_geode

    def get_max_ore_cost(self):
        """calc max ore cost"""
        ret = [self.ore[0], self.clay[0], self.obsidian[0], self.geode[0]]
        return max(ret)

    def __repr__(self) -> str:
        out_str = "Blueprint " + str(self.num) + "\n"
        out_str += "\tore: " + str(self.ore)+"\n"
        out_str += "\tclay: " + str(self.clay)+"\n"
        out_str += "\tobsidian: " + str(self.obsidian)+"\n"
        out_str += "\tgeode: " + str(self.geode)+"\n"
        out_str += "\tmax: " + str(self.get_max_ore_cost())
        return out_str


@dataclass(frozen=True)
class State():
    """represents State"""
    remaining: int

    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    ore_r: int = 1
    clay_r: int = 0
    obsidian_r: int = 0
    geode_r: int = 0


def parse_input_file():
    """parse input file"""
    blueprints = []

    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            line_split = line.strip().split(":")
            costs_split = [splitted.strip()
                           for splitted in line_split[1].split(".")]

            name = int(line_split[0].split(" ")[1])
            ore = [int(costs_split[0].split(" ")[4]), 0, 0, 0]
            clay = [int(costs_split[1].strip().split(" ")[4]), 0, 0, 0]

            obsidan_ore = int(costs_split[2].split(" ")[4])
            obsidan_clay = int(costs_split[2].split(" ")[7])
            obsidan = [obsidan_ore, obsidan_clay, 0, 0]

            geode_ore = int(costs_split[3].split(" ")[4])
            geode_obsidian = int(costs_split[3].split(" ")[7])
            geode = [geode_ore, 0, geode_obsidian, 0]

            blueprints.append(Blueprint(name, ore, clay, obsidan,  geode))

    return blueprints


def bfs(arg_blueprint: Blueprint, state: State):
    """exectute bfs"""
    best = 0
    frontier = deque([state])
    explored = set()

    while frontier:
        state = frontier.popleft()

        best = max(best, state.geode)
        if state.remaining == 0:
            continue

        max_ore_cost = arg_blueprint.get_max_ore_cost()

        ore_r = min(state.ore_r, max_ore_cost)
        clay_r = min(state.clay_r, arg_blueprint.obsidian[1])
        obs_r = min(state.obsidian_r, arg_blueprint.geode[2])

        ore = min(state.ore, state.remaining *
                  max_ore_cost - ore_r*(state.remaining-1))
        clay = min(state.clay, state.remaining *
                   arg_blueprint.obsidian[1] - clay_r*(state.remaining-1))
        obs = min(state.obsidian, state.remaining *
                  arg_blueprint.geode[2] - obs_r*(state.remaining-1))

        state = State(state.remaining,
                      ore, clay, obs, state.geode,
                      ore_r, clay_r, obs_r, state.geode_r)
        if state in explored:
            continue
        explored.add(state)

        # Don't make any robots; just accumulate
        frontier.append(State(state.remaining-1,
                              ore+ore_r, clay+clay_r, obs+obs_r, state.geode+state.geode_r,
                              ore_r, clay_r, obs_r, state.geode_r))

        if ore >= arg_blueprint.ore[0]:  # build ore robot
            frontier.append(State(state.remaining-1,
                                  ore-arg_blueprint.ore[0]+ore_r, clay +
                                  clay_r, obs+obs_r, state.geode+state.geode_r,
                                  ore_r+1, clay_r, obs_r, state.geode_r))
        if ore >= arg_blueprint.clay[0]:  # build clay robot
            frontier.append(State(state.remaining-1,
                                  ore-arg_blueprint.clay[0]+ore_r, clay +
                                  clay_r, obs+obs_r, state.geode+state.geode_r,
                                  ore_r, clay_r+1, obs_r, state.geode_r))
        # build obsidian robot
        if ore >= arg_blueprint.obsidian[0] and clay >= arg_blueprint.obsidian[1]:
            frontier.append(State(state.remaining-1,
                                  ore -
                                  arg_blueprint.obsidian[0]+ore_r,
                                  clay -
                                  arg_blueprint.obsidian[1]+clay_r,
                                  obs+obs_r, state.geode+state.geode_r,
                                  ore_r, clay_r, obs_r+1, state.geode_r))
        # build geode robot
        if ore >= arg_blueprint.geode[0] and obs >= arg_blueprint.geode[2]:
            frontier.append(State(state.remaining-1,
                                  ore -
                                  arg_blueprint.geode[0] +
                                  ore_r, clay+clay_r,
                                  obs -
                                  arg_blueprint.geode[2] +
                                  obs_r, state.geode+state.geode_r,
                                  ore_r, clay_r, obs_r, state.geode_r+1))

    return best


def solve_day19():
    """solve day19"""

    quality_level = 0
    geode_product = 1
    for blueprint in parse_input_file():
        geodes = bfs(blueprint, State(24))
        quality_level += geodes * blueprint.num

        if blueprint.num <= 3:  # First three blueprints; they start at 1
            geodes = bfs(blueprint, State(32))  # These take a while!
            geode_product *= geodes

    print("quality_level:", quality_level)
    print("geode_product:", geode_product)


solve_day19()
