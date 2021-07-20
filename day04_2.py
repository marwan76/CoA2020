import re
"""Advent of code day 4 second part"""
with open("day04_input.txt", 'r') as f:
    lines = f.readlines()
f.close()

def pass_validate(k, v):
    if k == "byr" and int(v) >= 1920 and int(v) <= 2002:
        return True
    if k == "iyr" and int(v) >= 2010 and int(v) <= 2020:
        return True

valid_pass = 0
new_valid_pass = 0
attribute_list = ["pid", "iyr", "eyr", "hgt", "hcl", "ecl", "byr"]

current = 0

for line in lines:
    if not line.strip():
        if current == len(attribute_list) and pass_validate(key, val):
            valid_pass += 1
        current = 0

    for field in line.strip().split():
        key, val = field.split(':')
        if key in attribute_list:
            current += 1


print(valid_pass)

