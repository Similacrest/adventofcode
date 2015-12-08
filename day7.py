#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 7 of AdventOfCode.com: trees, recursion, bitwise stuff"""
import re
from collections import defaultdict
import os


CONST_MODULO = 2 ** 16
CONST_MAX = CONST_MODULO - 1


class BitwiseOperationTree:
    """
    Represents a tree of bitwise ops over unsigned 16-bit integers
    """
    __ops = {
             None: {'argcount': 1, 'apply': lambda x: x[0]},
             # In NOT we won't use ~. ~ is for signed, don't want to use numpy types here.
             "NOT": {'argcount': 1, 'apply': lambda x: CONST_MAX - x[0]},
             "AND": {'argcount': 2, 'apply': lambda x: (x[0] & x[1]) % CONST_MODULO},
             "OR": {'argcount': 2, 'apply': lambda x: (x[0] | x[1]) % CONST_MODULO},
             "LSHIFT": {'argcount': 2, 'apply': lambda x: (x[0] << x[1]) % CONST_MODULO},
             "RSHIFT": {'argcount': 2, 'apply': lambda x: (x[0] >> x[1]) % CONST_MODULO}
            }

    def __init__(self):
        self.__circuits = defaultdict(lambda: {'args': [0], 'op': None})

    @classmethod
    def __verify(cls, arguments, op):
        """Verifies the arity of operations
        :param arguments: list of arguments: keyname string, int, or int string
        :param op: valid bitwise operation name
        """
        if len(arguments) != cls.__ops[op]['argcount']:
            raise ValueError("Wrong n-arity of {op}".format(op=op))

    def save(self, arguments, op, target):
        """
        :param arguments: list of arguments: keyname string, int, int string or None
        :param op: valid bitwise operation name
        :param target: key to save
        """
        arguments = [a for a in arguments if a is not None]
        self.__verify(arguments, op)
        for i in range(len(arguments)):
            if type(arguments[i]) == str and arguments[i].isdigit():
                arguments[i] = int(arguments[i])
        self.__circuits[target] = {'args': arguments, 'op': op}

    def get(self, item):
        """ Calculates a subtree by result
        :param item: keyname
        :return: int: result of subtree calculation
        """
        for i in range(len(self.__circuits[item]['args'])):
            if type(self.__circuits[item]['args'][i]) is str:
                self.__circuits[item]['args'][i] = self.get(self.__circuits[item]['args'][i])

#        print(self.__circuits[item]['op'], self.__circuits[item]['args'])
        return self.__ops[self.__circuits[item]['op']]['apply'](self.__circuits[item]['args'])

    def __getitem__(self, item):
        return self.get(item)


def main():
    """
    Save each line in the tree, calculate 'a', write the value into 'b' and calculate 'a' again
    """
    circuit_parsers = [BitwiseOperationTree(), BitwiseOperationTree()]

    write_regex = re.compile(r"([a-z\sA-Z0-9]+) -> ([a-z]+)")
    operation_regex = re.compile(r"(([a-z]+|[0-9]+)\s)?((AND|OR|LSHIFT|RSHIFT|NOT)\s)?([a-z]+|[0-9]+)")
    with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day7.txt", "r") as datafile:
        for line in datafile:
            write_regex_match = write_regex.match(line)
            if write_regex_match is not None:
                target = write_regex_match.group(2)
                operation_regex_match = operation_regex.match(write_regex_match.group(1))
                if operation_regex_match is not None:
                    op = operation_regex_match.group(4)
                    arguments = list(operation_regex_match.group(2, 5))
                    for p in circuit_parsers:
                        p.save(arguments, op, target)
    a_value = circuit_parsers[0]['a']
    print(a_value)

    a_value = [a_value]
    circuit_parsers[1].save(a_value, None, 'b')
    print(circuit_parsers[1]['a'])

if __name__ == '__main__':
    main()
