#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 4 of AdventOfCode.com: md5 hash bruteforcing"""
import os
import hashlib
import math


def adventcoin_mine(salt, zeros, prob=0.99):
    """MD5-hashes salt + counter, increasing counter until hash begins with a given number of 0's in HEX,
    or until maximum value is reached
    :param salt: string to append before countes
    :param zeros: number of zeros to search for
    :param prob: float between 0 and 1, we stop the search if we didn't find the value with this confidence interval
    :return: positive number that satisfies the condition, or 0 if the maximum value was exceeded
    """
    i = 0
    zeros_string = "".rjust(zeros, '0')

    if 1-prob > 1e-8:
        max_i = int(round(math.log(1-prob, 1-(1/16) ** zeros)))
    else:
        max_i = 0
    while True:
        if i > max_i > 0:  # max_i = 0 means we ignore maximum
            # We stop here
            return 0

        i += 1
        md5_hash = hashlib.md5((salt+str(i)).encode('utf8')).hexdigest()
        if md5_hash[:zeros] == zeros_string:
            break
    return i

with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day4.txt", "r") as datafile:
    data = datafile.read().replace('\n', '')

print(adventcoin_mine(data, 5))
print(adventcoin_mine(data, 6))
