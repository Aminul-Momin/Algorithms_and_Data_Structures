class DepthFirstSearchOrder:
    """
    The DepthFirstOrder class represents a data type for determining depth
    -first search ordering of the vertices in a digraph or edge-weighted digraph,
    including preorder, and postorder
    """
    def __init__(self, G, s):

        self.marked = {}  # marked[v] = has v been marked in dfs?
        self.pre = {}  # pre[v] = preorder  number of v
        self.post = {}  # post[v] = postorder number of v
        self.preorder_q = []  # Queue of vertices in preorder
        self.postorder_q = []  # Queue of vertices in postorder
        self.pre_counter = 0  # counter or preorder numbering
        self.post_counter = 0  # counter for postorder numbering

        # self.parent = {}       #
        # self.discovery_time = {}       #
        # self.finish_time = {}       #
        # self.time = 0     #

        self.dfs(G)

    def dfs(self, graph):
        for u in graph:
            if u not in self.marked:
                self.dfs_visit(graph, u)

    def dfs_visit(self, graph, u):
        """ Visits those neighbors of u which have not been visited yet

        Args:
            graph  -> the graph
            u      -> the vertex of which neighbors are to visit
        """
        self.pre_counter += 1
        self.marked[u] = True
        self.pre[u] = self.pre_counter
        self.preorder_q.append(u)

        for v in u.adj:
            if not self.marked[v]:
                self.dfs_visit(graph, v)

        self.post_counter += 1
        self.post[u] = self.post_counter
        self.postorder_q.append(u)
