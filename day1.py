import os


def count_floors(floor_string):
    floor = 0
    i = 0
    basement_enter = 0
    for char in floor_string:
        i += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0 and basement_enter == 0:
            basement_enter = i
    return {'Floor': floor, 'Basement first entered on step:': basement_enter}


with open(os.path.dirname(os.path.realpath('__file__')) + "/day1.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')
print(count_floors(data))
