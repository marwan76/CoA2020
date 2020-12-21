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
        minmax = line_to_split[0].split("-")
        new_line = (line_to_split[2])
        low = minmax[0]
        high = minmax[1]

        for num in range(1, len(new_line)+1):
            print(num)
            if replace_ch == new_line[int(low)] or replace_ch == new_line[int(high)]:
                my_count = my_count + 1
                break
    return my_count

RESULTS = valid_passwords(v)
print(RESULTS)
