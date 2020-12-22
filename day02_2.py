"""Code of Advent 2020 day 2"""

f = open("day02_input1.txt")
v = []
for s in f:
    v.append(s.strip("\n"))
f.close()


def valid_passwords(val):
    """Function that splits line by line and counts valid passwords"""
    my_count = 0

    for line in val:
        line_to_split = line.split()
        replace_ch = line_to_split[1].replace(":", "")
        low_high = line_to_split[0].split("-")
        new_line = (line_to_split[2])
        low = low_high[0]
        high = low_high[1]

        if (replace_ch == new_line[int(low)-1]) ^ (replace_ch == new_line[int(high)-1]):
            my_count = my_count + 1

    return my_count

RESULTS = valid_passwords(v)
print(RESULTS)
