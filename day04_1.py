"""Advent of code day 4 first part"""
with open("day04_input.txt", 'r') as f:
    lines = f.readlines()
f.close()
valid_pass = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

current = 0

for line in lines:
    if line == "\n":
        if current == len(fields):
            valid_pass += 1
        current = 0
        continue

    for field in line.split():
        key, val = field.split(':')
        if key in field:
            current += 1
print(valid_pass)
