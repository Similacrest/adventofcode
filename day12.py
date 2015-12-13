#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 12 of AdventOfCode.com: tree json traverse"""
import json
import os


def iterate(tree, ignore=None):
    """Find sum of ints in a tree-like structure
    :param tree: tree-like structure
    :param ignore: Value of property to ignore the structure
    :return: sum of all ints
    """
    if type(tree) is list:
        return sum([iterate(d, ignore) for d in tree])
    elif type(tree) is dict:
        if ignore is None or list(tree.values()).count(ignore) == 0:
            return sum([iterate(d, ignore) for d in tree.values()])
        else:
            return 0
    elif type(tree) is int:
        return tree
    else:
        return 0
 
with open(os.path.dirname(os.path.realpath(__file__)) + "/input/day12.txt", "r") as datafile:
    datastr = datafile.read()
    data = json.loads(datastr)

print(iterate(data))
print(iterate(data, "red"))

    
# print(sum(map(lambda x:int(x), re.findall(r"-?\d+", inp))))
