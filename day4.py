#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Day 4 of AdventOfCode.com: md5 hash bruteforcing"""
import os
import hashlib


def adventcoin_mine(salt, zeros):
    """MD5-hashes salt + counter, increasing counter until hash begins with a given number of 0's in HEX
    :param salt: string to append before countes
    :param zeros: number of zeros to search for
    :return: number that satisfies the condition
    """
    i = 1
    md5_hash = hashlib.md5((salt+"1").encode('utf8')).hexdigest()
    while md5_hash[:zeros] != "".rjust(zeros, '0'):
        i += 1
        md5_hash = hashlib.md5((salt+str(i)).encode('utf8')).hexdigest()
    return i

with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day4.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')

print(adventcoin_mine(data, 5))
print(adventcoin_mine(data, 6))
