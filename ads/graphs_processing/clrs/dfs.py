class DFS(object):
    """
    The DepthFirstSearch class represents a data type for determining the
    number of vertices connected to a given source vertex s in an undirected
    graph.
    """
    def __init__(self, G, s):
        """Initializes DFS .
        """
        self.marked = {}  # marked[v] = is there an s-v path?
        self.count = 0  # number of vertices connected to s

        for u in G:
            self.marked[u] = False

        self.dfs_visit(G, s)

    def dfs_visit(self, graph, s):
        """Visits those neighbors of u which have not been visited yet.

        Args:
            graph: The undirected graph.
            s    : The source vertex from which searching begins.
        """
        self.count += 1
        self.marked[s] = True
        for v in s.adj:
            if not self.marked[v]:
                self.dfs_visit(graph, v)

    def is_marked(self, v):
        return self.marked[v]

    def count_marked(self):
        return self.count
