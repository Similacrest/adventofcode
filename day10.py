#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 10 of AdventOfCode.com: What's common in between digits and nuclear decay?"""
import os


# ToDo: rewrite this one with groupby, and\or ConwayMendeleevTable, and\or multithreading
def look_and_say(numbers):
    """
    Performs a look'n'say iteration. Repeated digits are collapsed into one and preceeded by their amount.
    Add 1 before each single digit. '111' -> '31'
    :param numbers: string of digits
    :return: look'n'say op over digits
    """
    digit = ""
    result = ""
    count = 0
    for c in numbers:
        if c == digit:
            count += 1
        else:
            if count:
                result += str(count) + digit
            digit = c
            count = 1
    result += str(count) + digit
    return result


with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day10.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')
print(0, len(data))
for i in range(0, 79):
    data = look_and_say(data)
    print(i + 1, len(data))
