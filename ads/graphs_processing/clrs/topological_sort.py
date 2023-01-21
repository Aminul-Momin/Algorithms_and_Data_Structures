class TopologicalSort:
    def __init__(self, G):

        self.parent = {}  #
        self.order = []  #
        self.dfs(G)
        self.order.reverse()

    def dfs(self, graph):
        for vrtx in graph:
            if vrtx not in self.parent:
                self.dfs_visit(graph, vrtx)

    def dfs_visit(self, graph, u, parent=None):
        """Visits those neighbors of u which have not been visited yet
        
        Args:
            graph : The graph
            u     : The vertex of which neighbors are to visit
            parent: The parent vertex of u
        
        """
        self.parent[u] = parent
        for v in u.adj:
            if v not in self.parent:
                self.dfs_visit(graph, v, u)
        self.order.append(u.key)

    def topological_sort(self):
        return self.order
