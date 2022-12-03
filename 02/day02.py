"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""


def calc_game_score(you, opponent):
    """calc game score """
    ret_score = 0
    # A:     Rock        1 point
    # B:     Paper       2 points
    # C:     Scissors    3 points

    # draw
    if you == opponent:
        ret_score += 3

    if you == "A":
        if opponent == "C":
            ret_score += 6
        ret_score += 1

    elif you == "B":
        if opponent == "A":
            ret_score += 6
        ret_score += 2

    elif you == "C":
        if opponent == "B":
            ret_score += 6
        ret_score += 3
    else:
        print("Error")
    return ret_score


def solve_day2_part1():
    """solve day2"""
    with open("input.txt", encoding="utf-8") as input_file:
        score = 0
        for line in input_file:
            opponent = line[0].strip()
            you = line[2].strip()
            if you == "X":
                you = "A"
            elif you == "Y":
                you = "B"
            elif you == "Z":
                you = "C"
            score += calc_game_score(you, opponent)
    return score


def solve_day2_part2():
    """solve day2"""
    with open("input.txt", encoding="utf-8") as input_file:
        score = 0
        for line in input_file:
            opponent = line[0].strip()
            you = line[2].strip()

            # need to draw
            if you == "Y":
                you = opponent

            # need to win
            elif you == "X":
                if opponent == "A":
                    you = "C"
                elif opponent == "B":
                    you = "A"
                elif opponent == "C":
                    you = "B"

            # need to loose
            elif you == "Z":
                if opponent == "A":
                    you = "B"
                elif opponent == "B":
                    you = "C"
                elif opponent == "C":
                    you = "A"

            score += calc_game_score(you, opponent)

    return score


print("total score according to your strategy guide:", solve_day2_part1())
print("total score according to your strategy guide:", solve_day2_part2())
