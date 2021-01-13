"""Advent of code day 3"""
with open("day03_input1.txt", 'r') as f:
    lines = f.readlines()

CURR_X = 0

SLOPE_X = 3

TREES = 0

for curr_y, each_line in enumerate(lines):
    if each_line[CURR_X] == "#":
        print(each_line)
        TREES += 1
    CURR_X = (CURR_X + SLOPE_X) % len(each_line[:-1])
print(f"Solution 1:{TREES}")
