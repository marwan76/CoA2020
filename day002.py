"""Code of Advent 2020 day 1"""

f = open("day01_input1.txt")
v = []
for s in f:
    v.append(int(s.strip("\n")))
f.close()

for x in v:
    for y in v:
        for z in v:
            if x+y+z == 2020:
                print(x*y*z)
