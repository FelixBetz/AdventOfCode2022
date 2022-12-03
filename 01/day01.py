"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""


def solve_day1():
    """solve day1"""
    max_calories = []
    cnt_calories = 0

    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            if line == "\n":
                max_calories.append(cnt_calories)
                cnt_calories = 0  # reset cnt calories
            else:
                cnt_calories += int(line)

    return max_calories


calories = solve_day1()
calories.sort(reverse=True)

print("Elf carrying the most calories:", calories[0])
print("topy three Elfs carrying the most calories:", sum(calories[0:3]))
