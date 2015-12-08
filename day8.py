#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 8 of AdventOfCode.com: character counting"""

import re
import os


def main():
    """
    Check for \\, \* and \xhh
    """
    # Yeah, eval() would've simplified things, but... security, duh
    unescaped_count = 0
    escaped_count = 0
    reg = re.compile(re.escape(r'\\')+'|'+re.escape(r'\"')+'|'+re.escape('\\')+"x[0-9a-fA-F]{2}")
    with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day8.txt", "r") as datafile:
        for line in datafile:
            line = line.strip()
            matches = reg.findall(line)
            l = 2 + sum(len(s) for s in matches) - len(matches)
            unescaped_count += l
            escaped_count += line.count('\\') + line.count('\"') + 2

    print(unescaped_count, escaped_count)

if __name__ == '__main__':
    main()
