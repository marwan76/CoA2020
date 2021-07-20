"""Advent of code day 4 first part"""
with open("day04_input.txt", 'r') as f:
    lines = f.readlines()
f.close()
valid_pass = 0

attribute_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

current = 0

for line in lines:
    if not line.strip():
        if current == len(attribute_list):
            valid_pass += 1
        current = 0

    for field in line.strip().split():
        key, val = field.split(':')
        if key in attribute_list:
            current += 1
print(valid_pass)
