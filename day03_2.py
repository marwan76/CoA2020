"""Advent of code day 3"""
with open("day03_input1.txt", 'r') as f:
    lines = f.readlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
MULT_TREES = 1
for slope in slopes:
    print("Slope: ", slope)
    slope_x, slope_y = slope
    TREES = 0
    CURR_X = 0
    for curr_y, each_line in enumerate(lines):
        if curr_y % slope_y == 0:

            if each_line[CURR_X] == "#":
                TREES += 1
            CURR_X = (CURR_X + slope_x) % len(each_line[:-1])
    print("Trees on this slope: ", TREES)
    MULT_TREES *= TREES
print("Solution 2: ", MULT_TREES)
