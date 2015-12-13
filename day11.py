#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 11 of AdventOfCode.com: Password criteria"""
import re
import os
from functools import reduce


def inc(st, exclude="iol"):
    """Increase string by 1 char and return
    :param st: string to work with
    :param exclude: exclude these chars
    :return: string with increased chars
    """
    strlist = list(st)
    i = len(strlist) - 1
    while i >= 0:
        skip = 0
        if strlist[i] >= 'z':
            strlist[i] = 'a'
            i -= 1
        else:
            if strlist[i] in exclude:
                skip = 1
            strlist[i] = chr(ord(strlist[i]) + 1 + skip)
            return reduce(lambda x, y: x + y, strlist)
    return None


def main():
    """
    Check for regexes
    """
    with open(os.path.dirname(os.path.realpath(__file__)) + "/input/day11.txt", "r") as datafile:
        datastr = datafile.read().strip("\n")

    valid = \
        [re.compile(r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz"),
         re.compile(r"^[^iol]+$"), re.compile(r"(.)\1.*(.)\2")]

    for i in range(0, 2):
        while any([r.search(datastr) is None for r in valid]):
            datastr = inc(datastr)
        print(datastr)
        datastr = inc(datastr)
    # print([v.search("xyzabbcc") is None for v in valid])

if __name__ == '__main__':
    main()
