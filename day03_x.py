"""Code of Advent 2020 day 3"""

with open("day03_input1.txt", 'r') as f:
    v = f.readlines()
f.close()

START_x = 0
MOVE_x = 3
TREE_FOUND = 0

for line in v:
    if line[START_x] == "#":
        TREE_FOUND += 1
    START_x = (START_x + MOVE_x) % len(line[:-1])
print(f"Solution 1:{TREE_FOUND}")

"""Code of Advent 2020 day 3 exercise 2"""
