"""
The UndirectedCycle class represents a data type for determining whether a 
undirected graph has a cycle. The has_cycle() operation determines whether the 
undirected graph has a cycle and, if so, the cycle() operation returns one.
"""


class UndirectedCycle(object):
    def __init__(self, G):
        self._marked = {}
        self._edge_to = {}
        self._cycle = None

        for v in G:
            self._marked[v] = False
        if self._has_self_loop(G):
            return
        if self._has_parallel_edge(G):
            return

        for u in G:
            if not self._marked[u]:
                self.dfs_visit(G, u)

    def dfs_visit(self, graph, u, parent=None):
        """Visits those neighbors of u which have not been visited yet
        
        Args:
            graph: The graph
            u    : The vertex of which neighbors are to visit
        
        """
        self._marked[u] = True

        for v in u.neighbors():
            if self._cycle is not None:  # short circuit if cycle alredy found
                return
            elif not self._marked[v]:  # found new vertex, so recur
                self._edge_to[v] = u
                self.dfs_visit(graph, v, u)

            # check for cycle (but disregard reverse of edge leading to v)
            elif v != parent:
                self._cycle = []
                x = u
                while x != v:
                    self._cycle.append(x)
                    x = self._edge_to[x]
                self._cycle.append(v)
                self._cycle.append(u)

    def _has_self_loop(self, Graph):
        """ Checks if the specified graph has self-loop edges.
        """

        for u in Graph:
            for v in u.neighbors():
                if u == v:
                    self._cycle = []
                    self._cycle.append(u)
                    self._cycle.append(v)
                    return True
        return False

    def _has_parallel_edge(self, Graph):
        """Checks if the specified graph has parallel edges.
        """
        for u in Graph:
            # check for parallel edges incident to u
            for v in u.neighbors():
                if self._marked[v]:
                    self._cycle = []
                    self._cycle.append(u)
                    self._cycle.append(v)
                    self._cycle.append(u)
                    return True

                self._marked[v] = True

            for v in u.neighbors():
                self._marked[v] = False

        return False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        """Returns a directed cycle if the undirected graph has a directed cycle, and 
        null otherwise.
        
        Returns:
            a directed cycle as an iterable if the undirected graph has a directed cycle,
            and null otherwise
        """
        return self._cycle

    def check(self):
        """Certify that undirected graph has a directed cycle if it reports one
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
