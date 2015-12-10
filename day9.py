#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Day 9 of AdventOfCode.com: Dijkstra is, for sure, a difficult surname"""
import os
from copy import deepcopy


# ToDo: rewrite this one with multithreading and no copying and graph tools
def delete_graph_node(node, graph):
    """Returns copy graph with node deleted
    :param node: key of node to delete
    :param graph: target of graph
    :return: copy of graph with node deleted
    """
    new_graph = deepcopy(graph)
    for n in new_graph[node]:
        del new_graph[n][node]
    del new_graph[node]
    return new_graph


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
    with open(os.path.dirname(os.path.realpath('__file__')) + "/input/day9.txt", "r") as datafile:
        for line in datafile:
            (source, _, dest, _, distance) = line.split()
            for city in (source, dest):
                if city not in cities:
                    cities[city] = {}
            cities[source][dest] = cities[dest][source] = float(distance)

        print(hamilton_path_len(cities, min))
        print(hamilton_path_len(cities, max))

if __name__ == '__main__':
    main()
