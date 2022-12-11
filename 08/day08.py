"""
--- Day 8 Supply Stacks  ---
https://adventofcode.com/2022/day/8
"""


def max_empty(arg_list):
    """return the max element of a list, return -1 if list is empty"""
    if len(arg_list) == 0:
        return -1
    return max(arg_list)


def get_col(arg_tree, arg_idx):
    """returns colum as list"""
    ret_row = []
    for row in arg_tree:
        ret_row.append(row[arg_idx])

    return ret_row


def is_visible(arg_tree, arg_left, arg_right, arg_top, arg_bot):
    """check if a tree is visible in either of the 4 directions"""
    compare = [arg_left, arg_right, arg_top, arg_bot]
    for comp in compare:
        if arg_tree > max_empty(comp):
            return 1
    return 0


def calc_scenic_score(arg_tree, arg_left, arg_right, arg_top, arg_bot):
    """calc the scenic score for a tree"""
    ret_score = 1
    if len(arg_left) > 0:
        arg_left.reverse()
    if len(arg_top) > 0:
        arg_top.reverse()

    compare = [arg_left, arg_right, arg_top, arg_bot]
    for comp in compare:
        if len(comp) == 0:
            ret_score = 0
            break
        cnt = 0
        for tree in comp:
            if arg_tree > tree:
                cnt += 1
            if arg_tree <= tree:
                cnt += 1
                break
        ret_score *= cnt
    return ret_score


def solve_day8():
    """solve day8"""
    cnt_visible = 0
    max_scenic_score = 0
    trees = []
    with open("input.txt", encoding="utf-8") as input_file:
        for line in input_file:
            row = []
            for tree in line.strip():
                row.append(int(tree))
            trees.append(row)

    for i, row in enumerate(trees):
        for k, tree in enumerate(row):
            left = row[:k]
            right = row[k+1:]

            col = get_col(trees, k)
            top = col[:i]
            bot = col[i+1:]
            cnt_visible += is_visible(tree, left, right, top, bot)

            # calc scenic score

            scenic_score = calc_scenic_score(tree, left, right, top, bot)
            max_scenic_score = max(scenic_score, max_scenic_score)

    print("how many trees are visible:", cnt_visible)
    print(" highest scenic score:", max_scenic_score)


solve_day8()
