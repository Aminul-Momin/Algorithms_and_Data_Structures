''' Not implemented yet
'''

from ads.graphs_processing.clrs import GenerateGraph as GG
from random import randint, choice
import sys


class CycleDetection(object):

    def __init__(self, G):

        self.parent = {}           #
        self.discovery_time = {}   #
        self.finish_time = {}       #
        self.time = 0              #

        self.dfs(G)

    def dfs(self, graph):
        for u in graph:
            if u not in self.parent:
                self.dfs_visit(graph, u)

    def dfs_visit(self, graph, u, parent=None):
        ''' Visits those neighbors of u which have not been visited yet

        Args:
            graph  -> the graph
            u      -> the vertex of which neighbors are to visit
            parent -> the parent vertex of u

        '''
        self.time += 1
        self.parent[u] = parent
        self.discovery_time[u] = self.time

        for v in u.adj:
            if v not in self.parent:
                self.dfs_visit(graph, v, u)

        self.time += 1
        self.finish_time[u] = self.time

    # def show_path(self):
    #     for vrtx in self.parent:
    #         path = []
    #         x = self.parent[vrtx]
    #         while x is not None:
    #             path.append(x.vrtx)
    #             x = self.parent[x]
    #         path.reverse()
    #         path = ' -> '.join([str(i) for i in path])
    #         print(
    #             "Path: (first vertex in the graph --> {})\t".format(self.parent[vrtx].key), path)


def test_CycleDetection(data):

    if type(data) is str:
        G = GG.digraph_from_file(data)
    else:
        G = GG.digraph_from_collection(data)

    s = G.get_vertex(choice(list(G.vertics.keys())))
    t = G.get_vertex(choice(list(G.vertics.keys())))
    search = CycleDetection(G)
    print("The shortest path({} --> {}): ".format(s.key, t.key))
    # print("\t", search.show_path())

    # print(G.outdegree(s.key))
    # print(G.outdegree(t.key))


if __name__ == '__main__':
    file = "tinyEWD.txt"

    graph = {
        'A': {'B': 20, 'D': 80, 'G': 90},
        'B': {'F': 10},
        'F': {'C': 10, 'D': 40},
        'C': {'F': 50, 'D': 10, 'H': 20},
        'D': {'G': 20, 'C': 10},
        'H': {},
        'G': {'A': 20},
        'E': {'B': 50, 'G': 30}
    }

    # Shortest Path ('B' --> 'A'): B -> F -> C -> D -> G -> A
    # Shortest Path ('B' --> 'A'): B -> F -> C -> D

    if len(sys.argv) > 1:
        test_CycleDetection(sys.argv[1])
    else:
        test_CycleDetection(graph)
