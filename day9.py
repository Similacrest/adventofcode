#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 9 of AdventOfCode.com: Dijkstra is, for sure, a difficult surname"""
import re
import os
from functools import lru_cache
from copy import deepcopy


def delete_graph_node(node, graph):
    """Returns copy graph with node deleted
    :param node: key of node to delete
    :param graph: target of graph
    :return: copy of graph with node deleted
    """
    gr = deepcopy(graph)
    for n in gr[node]:
        del gr[n][node]
    del gr[node]
    return gr


def hamilton_path_from_start_len(start, graph, selector=min):
    """Recursive; calculate length of path traversing all nodes starting with given node
    :param start: node from with to start the path
    :param graph: target graph
    :param selector: function that selects length from all possible paths
    :return: length of the path
    """
    if len(graph) and len(graph[start]):
        return selector([graph[start][n] + hamilton_path_from_start_len(n, delete_graph_node(start, deepcopy(graph)),
                                                                        selector) for n in graph[start]])
    else:
        return 0


def hamilton_path_len(graph, selector=min):
    """ calculate length of path traversing all nodes
    :param graph: target graph
    :param selector: function that selects length from all possible paths
    :return: length of the path
    """
    return int(round(selector([hamilton_path_from_start_len(start, graph, selector) for start in graph])))


def main():
    """
    read graph, find min and max paths
    """
    cities = {}
    data_regex = re.compile("([A-Za-z]+) to ([A-Za-z]+) = (\d+)")
    with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day9.txt", "r") as datafile:
        for line in datafile:
            data_regex_match = data_regex.match(line)
            if data_regex_match is not None:
                for k in range(1, 3):
                    if data_regex_match.group(k) not in cities:
                        cities[data_regex_match.group(k)] = {}
                    cities[data_regex_match.group(k)][data_regex_match.group(3-k)] = \
                        float(data_regex_match.group(3))

        print(hamilton_path_len(cities, min))
        print(hamilton_path_len(cities, max))
if __name__ == '__main__':
    main()
