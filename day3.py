#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 3 of AdventOfCode.com: traversing and extending matrices"""
import os
import numpy as np
import math


def count_visited_houses(moves, performers=1):
    """
    :param moves: string of '^' (up), 'V' (down), '<' (left), '>' (right) characters,
    which represent instructions for all performers
    :param performers: positive integer that determines how many performers are doing instructions in turns
    :return: amount of cells visited by at least 1 performer at least once
    """
    count = 0
    current_performer = 0
    width = 11
    height = 11

    if performers <= 0:
        return 0

    x = np.full(performers, int(math.floor(width / 2)), dtype=int)
    y = np.full(performers, int(math.floor(height / 2)), dtype=int)
    houses = np.zeros((width, height), dtype=int)

    houses[y[0], x[0]] += performers
    count += 1

    for move in moves:
        if move == '^':
            y[current_performer] += 1
        elif move == 'v':
            y[current_performer] -= 1
        elif move == '<':
            x[current_performer] -= 1
        elif move == '>':
            x[current_performer] += 1

        if x[current_performer] < 0:
            houses = np.insert(houses, 0, [0], axis=1)
            width += 1
            x += 1  # shift all
        elif x[current_performer] >= width:
            houses = np.insert(houses, width, [0], axis=1)
            width += 1
        elif y[current_performer] < 0:
            houses = np.insert(houses, 0, [0], axis=0)
            height += 1
            y += 1  # shift all
        elif y[current_performer] >= height:
            houses = np.insert(houses, height, [0], axis=0)
            height += 1

        if houses[y[current_performer], x[current_performer]] == 0:
            count += 1
        houses[y[current_performer], x[current_performer]] += 1

        current_performer += 1
        if current_performer >= performers:
            current_performer = 0

    return count


with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day3.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')
print(count_visited_houses(data, 1))  # Santa
print(count_visited_houses(data, 2))  # Santa + RoboSanta
