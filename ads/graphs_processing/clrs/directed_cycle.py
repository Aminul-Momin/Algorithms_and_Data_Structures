#!/usr/bin/env python
"""
The DirectedCycle class represents a data type for determining whether a
digraph has a directed cycle. The hasCycle operation determines whether the
digraph has a simple directed cycle and, if so, the cycle operation returns one.
"""


class DirectedCycle(object):
    def __init__(self, G):
        self._marked = {}
        self._parent = {}
        self._on_stack = {}
        self._cycle = None

        for v in G:
            self._marked[v] = False
            self._on_stack[v] = False

        for u in G:
            if not self._marked[u] and self._cycle == None:
                self.dfs_visit(G, u)

    # check that algorithm computes either the topological order or finds a directed cycle
    def dfs_visit(self, graph, u):
        """Visits those neighbors of u which have not been visited yet

        Args:
            graph: The graph
            u    : The vertex of which neighbors are to visit

        """
        self._marked[u] = True
        self._on_stack[u] = True

        for v in u.adj:
            if self._cycle is not None:  # short circuit if directed cycle found
                return
            elif not self._marked[v]:  # found new vertex, so recur
                self._parent[v] = u
                self.dfs_visit(graph, v)

            elif self._on_stack[v]:  # trace back directed cycle
                self._cycle = []
                x = u
                while x != v:
                    self._cycle.append(x)
                    x = self._parent[x]
                self._cycle.append(v)
                self._cycle.append(u)

        self._on_stack[u] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        """Returns a directed cycle if the digraph has a directed cycle, and
        null otherwise.

        Returns:
            a directed cycle as an iterable if the digraph has a directed cycle,
            and null otherwise
        """
        return self._cycle

    def check(self):
        """ Certify that digraph has a directed cycle if it reports one
        """
        if self.has_cycle():  # verify cycle
            first, last = -1, -1
            for v in self._cycle:
                if (first == -1):
                    first = v
                last = v

            if first != last:
                print("cycle begins with {} and ends with {}".format(
                    first, last))
                return False
        return True
