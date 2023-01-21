from ads.errors.exceptions import NegativeWeightCycleException
from .graphs import Digraph, DGVertex


class BellmanFord(object):
    """
    The class represents a data type for detecting the negative-weight cycle for
    single-source shortest paths problem in edge-weighted digraphs.

    It returns True if no negative-weight cycle if detected or False if a negative
    cycle reachable from the source vertex.

    NOTE: The edge weights can be positive, negative, or zero.
    """
    def __init__(self, G: Digraph, source: DGVertex):
        self._bellman_ford(G, source)

    def _bellman_ford(self, G: Digraph, source: DGVertex) -> bool:
        """Check whether the given digraph has negative-weight cycle or not.

        Args:
            G (Digraph): A directed graph.
            source (DGVertex): a special vertex for directed graph.

        Returns:
            bool: True if no negative-weight cycle reachable from source,
                False otherwise.
        """

        source.distance = 0

        for _ in range(G.V() - 1):
            for u in G:
                for v in u.neighbors():
                    self.relax(u, v)

        # Check for negative-weight cycles
        for u in G:
            for v in u.neighbors():
                if v.distance > u.distance + u.adj[v]:
                    return False
        return True

    def relax(self, u, v):
        """Relax the edge between u and v and update distance of v.

        Args:
            u: a vertex, predecessor of v
            v: a vertex, decendent of u
        """
        # Shortest distane so far: ∂(s, v) = distance[u] + u_v_weight
        if v.distance > u.distance + u.adj[v]:
            v.distance = u.distance + u.adj[v]
            v.parent = u
