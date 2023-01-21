class EdgeClasification(object):
    def __init__(self, G):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.t = 0

        self.dfs(G)

    def dfs(self, g):
        for vertex in g:
            if vertex not in self.parent:
                self.dfs_visit(g, vertex)
        return self

    def dfs_visit(self, g, v, parent=None):
        self.parent[v] = parent
        self.t += 1
        self.start_time[v] = self.t
        if parent:
            self.edges[(parent, v)] = 'Tree Edge'
        for w in v.neighbors():
            if w not in self.parent:  # n is not visited.
                self.dfs_visit(g, w, v)
            elif w not in self.finish_time:
                self.edges[(v, w)] = 'Back Edge'
            elif self.start_time[v] < self.start_time[w]:
                self.edges[(v, w)] = 'Forward Edge'
            else:
                self.edges[(v, w)] = 'Cross Edge'
        self.t += 1
        self.finish_time[v] = self.t

    def class_of_edges(self):
        # return [e for e in self.edges]
        pass
