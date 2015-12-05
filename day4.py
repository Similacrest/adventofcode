#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Day 4 of AdventOfCode.com: md5 hash bruteforcing"""
import os
import hashlib


def adventcoin_mine(salt, zeros, margin_coefficient=4):
    """MD5-hashes salt + counter, increasing counter until hash begins with a given number of 0's in HEX,
    or until maximum value is reached
    :param salt: string to append before countes
    :param zeros: number of zeros to search for
    :param margin_coefficient: is multiplied by 16^zeroes to get the maximum value; set it to 0 to search indefinitely
    :return: positive number that satisfies the condition, or 0 if the maximum value was exceeded
    """
    i = 0
    zeros_string = "".rjust(zeros, '0')
    max_i = int(round(pow(16, zeros) * margin_coefficient))

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
