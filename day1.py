#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 1 of AdventOfCode.com: simple loops"""
import os


def move_over_floors(instructions):
    """Moves over floors up and down by given instructions
    :param instructions: string of '(' (up) and ')' (down) characters
    :return: floor: number of floor where we stop
             basement_enter: number of first instruction where we entered negative values
    """
    floor = 0
    i = 0
    basement_enter = 0
    for char in instructions:
        i += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0 and basement_enter == 0:
            basement_enter = i
    return floor,  basement_enter


with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day1.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')
print(move_over_floors(data))
