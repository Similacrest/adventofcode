#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 6 of AdventOfCode.com: operating over matrices by commands... again"""
import os
import numpy as np
import re
from abc import ABCMeta, abstractmethod


class LightsArray(object):
    """
    Represents an abstract array of 'lights' that accept operations
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def on(self, target):
        """
        On operation abstraction
        :param target: 2D slice
        """
        pass

    @abstractmethod
    def off(self, target):
        """
        Off operation abstraction
        :param target: 2D slice
        """
        pass

    @abstractmethod
    def toggle(self, target):
        """
        Toggle operation abstraction
        :param target: 2D slice
        """
        pass

    @abstractmethod
    def value(self):
        """
        Value abstraction
        :return: some number characteristic of lightarray
        """
        return 0

    def perform(self, op, slice_start, slice_end):
        """
        Performs an operation over an array slice
        :param op: string 'turn on', 'turn off', 'toggle'
        :param slice_start: (x, y) tuple describing slice start coordinates
        :param slice_end: (x, y) tuple describing slice start coordinates
        """
        target = slice(slice_start[0], slice_end[0] + 1), slice(slice_start[1], slice_end[1] + 1)
        if op == 'turn on':
            self.on(target)
        elif op == 'turn off':
            self.off(target)
        elif op == 'toggle':
            self.toggle(target)


class BoolLightsArray(LightsArray):
    """
    Represents an array of 'lights' that can be On or Off and accept operations
    """
    def __init__(self, x=1000, y=1000):
        super().__init__()
        self.__lights = np.zeros((x, y), dtype=bool)

    def on(self, target):
        """
        On operation on bool array, enables light
        :param target: 2D slice
        """
        self.__lights[target] = True

    def off(self, target):
        """
        Off operation on bool array, disables light
        :param target: 2D slice
        """
        self.__lights[target] = False

    def toggle(self, target):
        """
        Toggle operation on bool array, toggles light
        :param target: 2D slice
        """
        self.__lights[target] = ~self.__lights[target]

    def value(self):
        """
        Value of boolarray
        :return: number of lights currently on
        """
        return np.count_nonzero(self.__lights)


class IntLightsArray(LightsArray):
    """
    Represents an array of 'lights' that have integer brightness and accept operations
    """
    def __init__(self, x=1000, y=1000):
        super().__init__()
        self.__lights = np.zeros((x, y), dtype=int)

    def on(self, target):
        """
        On operation on int array, increases brightness
        :param target: 2D slice
        """
        self.__lights[target] += 1

    def off(self, target):
        """
        Off operation on int array, decreases brightness or switches the light off
        :param target: 2D slice
        """
        self.__lights[target] = np.vectorize(lambda x: x-1 if x > 0 else 0)(self.__lights[target])

    def toggle(self, target):
        """
        Toggle operation on int array, greatly increases brightness for some reason
        :param target: 2D slice
        """
        self.__lights[target] += 2

    def value(self):
        """
        Value of int array
        :return: total brightness of lights
        """
        return np.sum(self.__lights)

op_regex = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

lights = BoolLightsArray(1000, 1000), IntLightsArray(1000, 1000)

with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day6.txt", "r") as datafile:
    for line in datafile:
        matched = op_regex.search(line)
        if matched is not None:
            operation = matched.group(1)
            start = [int(coord) for coord in matched.group(2, 3)]
            end = [int(coord) for coord in matched.group(4, 5)]
            for la in lights:
                la.perform(operation, start, end)

    for la in lights:
        print(la.value())
