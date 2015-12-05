#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 5 of AdventOfCode.com: regex matching"""
import re
import os


class RegexMatchCounter:
    """This class counts strings which satisfy all specified regular expressions

    """
    def __init__(self, regex_strings):
        """The constructor needs a list of valid regular expressions.
        :param regex_strings: list of valid regular expressions to be matched"""
        self.__regexes = [re.compile(regex) for regex in regex_strings]
        self.__count = 0

    def check(self, target):
        """This method checks its string argument against regexes and, if all of them matched, increases the counter
        :param target: string to be matched
        """
        if all(reg.search(target) is not None for reg in self.__regexes):
            self.__count += 1

    def count(self):
        """:return: the current value of how many strings have matched regexes
        """
        return self.__count


matchers = [
 RegexMatchCounter([r'([aeiou].*){3}', r'(.)\1', r'^((?!(ab)|(cd)|(pq)|(xy)).)*$']),
 RegexMatchCounter([r'(..).*\1',                  r'(.).\1'])
]

with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day5.txt", "r") as datafile:
    for line in datafile:
        for matcher in matchers:
            matcher.check(line)
for matcher in matchers:
    print(matcher.count())
