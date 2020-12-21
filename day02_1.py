"""Code of Advent 2020 day 2"""

file = open("day02_input1.txt")
v = []
for s in file:
    v.append(s.strip("\n"))
file.close()


def valid_password(val):
    """Function that splits line by line and counts valid passwords removes char"""
    my_count = 0
    for line in val:
        line_to_split = line.split()
        replace_ch = line_to_split[1].replace(":", "")
        minmax = line_to_split[0].split("-")
        low = minmax[0]
        high = minmax[1]
        compare_if_between = line_to_split[2].count(replace_ch)
        if int(low) <= compare_if_between <= int(high):
            my_count = my_count+1
    return my_count


RESULTS = valid_password(v)
print(RESULTS)
