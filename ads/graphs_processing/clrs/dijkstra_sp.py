#!/usr/bin/env python

import os
from typing import Dict

from ads.heaps.priority_queue import PriorityQueue
from ads.fundamentals.stack import Stack
from ads.graphs_processing.clrs.graphs import DGVertex, Digraph
from ads.graphs_processing.algs4.edge import Edge
from ads.stdlib.instream import InStream


class DSPVertex(DGVertex):
    """This Class represents a special vertex intended to be used with Dijkstra
    Shortes Path algorithm. The only reason it is special because it delegates
    comparison to it's distance wherase it's super class delegates comparison
    to it's key.

    Args:
        Vertex (DGVertex): The special vertex of Directed Graph.
    """
    def __init__(self, key):
        """Initializes DSPVertex by the given 'key'.

        Args:
            key (Any): The key of this vertex.
        """
        super(DSPVertex, self).__init__(key)
        self._distance = float('inf')

    def __lt__(self, other):
        # Delegate comparison to distance.
        return (self._distance < other._distance
                or (self._distance == other._distance
                    and id(self._adj) < id(other._adj)))

    def __le__(self, other):
        # Delegate comparison to distance.
        return (self._distance < other._distance
                or (self._distance == other._distance
                    and id(self._adj) <= id(other._adj)))

    def __gt__(self, other):
        # Delegate comparison to distance.
        return (self._distance > other._distance
                or (self._distance == other._distance
                    and id(self._adj) > id(other._adj)))

    def __ge__(self, other):
        # Delegate comparison to distance.
        return (self._distance > other._distance
                or (self._distance == other._distance
                    and id(self._adj) >= id(other._adj)))

    def __str__(self):
        return str(f"""DSPVertex({self._key})""")


class DijkstraSP(object):
    """
    This class represents a data type for solving the single-source shortest
    paths problem in edge-weighted digraph.
    NOTE: The edge-weights are nonnegative.
    """
    def __init__(self, G: Digraph, source: DSPVertex):
        """Initializes a DijkstraSP object to compute shortest.

        Args:
            G     : The Digraph without negetive cycle.
            source: The source (starting) vertex
        """
        self._pq: PriorityQueue = PriorityQueue()  # priority queue of vertices
        self.build_path(G, source)

    def build_path(self, G: Digraph, source: DSPVertex):
        """Build the shortest path from source to every other vertex."""

        source._distance = 0
        self._pq.insert(source)

        while not self._pq.is_empty():
            u = self._pq.extract_min()
            for v in u.adj():
                self.relax(u, v)

    def relax(self, u: DSPVertex, v: DSPVertex):
        """Relax the edge between u and v.

        Args:
            u: A vertex from which the edge originates.
            v: A vertex toward which the edge goes.
        """
        v_dist = u._distance + u.weight(v)

        if v_dist < v._distance:
            v._parent = u
            v._distance = v_dist

            if v in self._pq:
                self._pq.decrease_key(v)
            else:
                self._pq.insert(v)

    def has_path_to(self, v: DSPVertex) -> bool:
        return v._parent is not None

    def _derive_path(self, target: DSPVertex) -> Stack:
        """It builds shortest path from the stack of shortest path elements."""
        path = Stack()

        cur = target
        while cur._parent is not None:
            e = Edge(cur._parent._key, cur._key,
                     round(cur._parent.weight(cur), 2))
            path.push(e)
            cur = cur._parent

        return path

    def path_to(self, v: DSPVertex):
        return self._derive_path(v)


def main():
    data_file = "Algorithms_and_Data_Structures/data/tinyEWD.txt"
    DATA_FILE_PATH = os.path.abspath(os.path.join(os.pardir, data_file))
    stream = InStream(DATA_FILE_PATH)
    g = Digraph.from_stream(stream, vertex_type=DSPVertex)
    s = g.get_vertex(0)
    sp = DijkstraSP(g, s)

    for t in g.vertices():
        if sp.has_path_to(t):
            print(f"""{s._key} to {t._key} ({round(t._distance, 2)})""",
                  end="\t")
            for e in sp.path_to(t):
                print(e, end="\t")
            print()
        else:
            print(f"""{s._key} to {t._key} ( NO PATH!)""", end="\n")


if __name__ == "__main__":
    main()
