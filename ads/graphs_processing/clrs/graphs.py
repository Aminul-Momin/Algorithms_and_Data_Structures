from typing import List, Tuple, Dict, Optional, Generic, TypeVar, Iterable

T = TypeVar('T')


class Vertex(Generic[T]):
    """ The basic Vertex object to be used with graph object. """
    def __init__(self, key: T):
        """Initializes a Vertex with the given 'key'.

        Args:
            key (T): the key of this vertex
        """
        self._key: T = key  # the key of this vertex

        ## self._adj[v] = weight of the edge from this vertex to vertex, v.
        self._adj: Dict[Optional['Vertex'], int] = {}

    def add_neighbor(self, x, weight=1) -> None:
        """Insert the given vertex (x) into the adjacent list of this vertex.
        
        Args:
            x  (Vertex): The vertex to be added into the adjacent list.
            weight (Optional[int]): The weight of the given vertex.
        """
        self._adj[x] = weight

    def outdegree(self):
        """Count the number of vertex connected from this vertex.

        Returns:
            int: The number of vertex connected from this vertex.
        """
        return len(self._adj)

    def weight(self, x):
        """Compute the the weight of the edge between this vertex and 'x'.
        
        Args:
            x (Vertex): The vertex whose weight to be computed.
        Return:
            int: The weight of this vertex.
        """
        return self._adj[x]

    def adj(self) -> Iterable['Vertex']:
        """Collects all the vertices adjacent from this vertex.
        
        Returns:
            Iterable (Vertex): Collection of vertices.
        """
        return self._adj.keys()

    #************************ Python Special Methods: ************************#
    def __str__(self):
        return str(f"""Vertex({self._key})""")
        # return str(self._key) + ' : ' + str([x._key for x in self._adj])

    def __iter__(self):
        return iter(self._adj)

    def __hash__(self):  # will allow vertex to be a map/set key
        return hash(id(self))

    def __lt__(self, other):
        # Delegate comparison to key.
        return (self._key < other._key
                or (self._key == other._key and id(self._adj) < id(other.adj)))

    def __le__(self, other):
        # Delegate comparison to key.
        return (self._key < other._key or
                (self._key == other._key and id(self._adj) <= id(other.adj)))

    def __gt__(self, other):
        # Delegate comparison to key.
        return (self._key > other._key
                or (self._key == other._key and id(self._adj) > id(other.adj)))

    def __ge__(self, other):
        # Delegate comparison to key.
        return (self._key > other._key or
                (self._key == other._key and id(self._adj) >= id(other.adj)))

    #********************* End of Python Special Methods *********************#


class DGVertex(Vertex):
    """This class represents a Vertex object intended to be used with Directed Graph"""
    def __init__(self, key: T):
        super(DGVertex, self).__init__(key)
        self._indegree: int = 0  # indegree, number of edges incident to this vertex.
        self._parent: 'DGVertex' = None  # predecessor of this vertex

    def increase_indeg(self):
        self._indegree += 1

    def indegree(self):
        return self._indegree

    def __str__(self):
        return str(f"""DGVertex({self._key})""")


class Graph(object):
    def __init__(self, vrtx: Optional[Vertex] = Vertex):
        """Creates an empty Graph."""
        self._Vertex = vrtx  # the vertex object to be used into this graph
        self._vertics: Dict[T, Vertex] = {}  # vertices of this graph
        self._V: int = 0  # number of total vertices
        self._E: int = 0  # number of total edges

    def add_vertex(self, key: T):
        """Insert the given key into the adjacent list of this graph.
        
        Args:
            key: The key to be added into this Graph.
        """
        x = self._Vertex(key)
        self._vertics[key] = x
        self._V += 1

    def get_vertex(self, key: T) -> Vertex:
        """Gets the vertex associated with the given key.
        
        Args:
            key: The key of the vertex to be returned.
        
        Returns:
            Vertex: the vertex associated with the given key.
        """
        if key in self._vertics: return self._vertics[key]
        else: return None

    def add_edge(self, key_from: T, key_toward: T, cost=1):
        """ Add the edege associated with the given keys.
        
        Args:
            key_from (T)  : The key of the starting vertex.
            key_toward (T): The key of the ending vertex.
            cost (int): The weight of this edge.
        """
        if key_from not in self._vertics:
            self.add_vertex(key_from)
        if key_toward not in self._vertics:
            self.add_vertex(key_toward)
        self._vertics[key_from].add_neighbor(self._vertics[key_toward], cost)
        self._vertics[key_toward].add_neighbor(self._vertics[key_from], cost)
        self._E += 1

    def edges(self) -> List[Tuple[T, Vertex]]:
        """Collects all the edges of this graph as iterable.

        Returns:
            The iterable of edges.
        """
        list_of_edges = []
        for vrtx in self._vertics.values():
            for neighbor in vrtx.adj():
                list_of_edges.append((vrtx._key, neighbor))
        return list_of_edges

    def vertices(self) -> Iterable[Vertex]:
        """Creates a iterable of all the vertices of this graph.

        Returns:
            Iterable[Vertex]: A iterable of all the vertices of this graph.
        """
        return self._vertics.values()

    #************************ Python Special Methods: ************************#
    def __iter__(self):
        return iter(self._vertics.values())

    def __str__(self):
        return '\n'.join(
            [str(u._key) + ':  ' + str(self._display(u)) for u in self])

    def _display(self, u):
        e = {}
        for v in u.adj():
            e[v._key] = u.weight(v)
        return e

    #********************* End of Python Special Methods *********************#

    @staticmethod
    def from_file(file):
        """Generates a graph from the specified input stream. The format is
        the number of vertices V, followed by the number of edges E, followed
        by E pairs of vertices, with each entry separated by whitespace.
        
        Returns:
            Graph: new Graph from the given file.
        """

        graph = Graph()
        line_num = 0
        with open(file, encoding="utf-8") as f:
            while True:
                line = f.readline()
                line_num += 1
                if not line:
                    break
                if line_num != 1 and line_num != 2:
                    L = line.split()
                    graph.add_edge(int(L[0]), int(L[1]))
        return graph

    @staticmethod
    def from_stream(stream, vertex_type=None):
        """Generates a graph from the specified input stream. The format is
        the number of vertices V, followed by the number of edges E, followed
        by E pairs of vertices, with each entry separated by whitespace.

        Args:
            stream (InStream): the input stream.
        
        Returns:
            Graph: new Graph from stream.
        
        Raises:
            ValueError: if the endpoints of any edge are not in prescribed range.
            ValueError: if the number of vertices or edges is negative.
            ValueError: if the input stream is in the wrong format.

        """
        V = stream.readInt()  # read the number of vertices
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        g = Graph() if not vertex_type else Graph(vertex_type)
        E = stream.readInt()  # read the number of edges
        if E < 0:
            raise ValueError("Number of edges in a Graph must be nonnegative")
        for _ in range(E):
            v = stream.readInt()  # read the first vertex
            w = stream.readInt()  # read the second vertex
            weight = stream.readFloat()
            g.add_edge(v, w, weight)
        return g


class Digraph(Graph):
    def __init__(self, vrtx: Optional[DGVertex] = DGVertex):
        """Generates an empty Directed Graph."""
        super(Digraph, self).__init__(vrtx)

    def indegree(self, key: T):
        return self._vertics[key].indegree()

    def outdegree(self, key: T):
        return self._vertics[key].outdegree()

    def add_edge(self, key_from: T, key_toward: T, cost: int = 1):
        """ Add the edege associated with the given keys.
        
        Args:
            key_from (T)  : The key of the starting vertex.
            key_toward (T): The key of the ending vertex.
            cost (int): The weight of this edge.
        """
        if key_from not in self._vertics:
            self.add_vertex(key_from)
        if key_toward not in self._vertics:
            self.add_vertex(key_toward)
        self._vertics[key_from].add_neighbor(self._vertics[key_toward], cost)
        self._vertics[key_toward].increase_indeg()
        self._E += 1

    @staticmethod
    def from_file(file):
        """Generates a graph from the specified input stream. The format is
        the number of vertices V, followed by the number of edges E, followed
        by E pairs of vertices, with each entry separated by whitespace.
        
        Returns:
            Digraph: new Digraph from the given file.
        """

        graph = Digraph()
        line_num = 0
        with open(file, encoding="utf-8") as f:
            while True:
                line = f.readline()
                line_num += 1
                if not line:
                    break
                if line_num != 1 and line_num != 2:
                    L = line.split()
                    graph.add_edge(int(L[0]), int(L[1]), int(L[2]))
        return graph

    @staticmethod
    def from_stream(stream, vertex_type=None):
        """Generates a graph from the specified input stream. The format is
        the number of vertices V, followed by the number of edges E, followed
        by E pairs of vertices, with each entry separated by whitespace.

        Args:
            stream (InStream): the input stream.
        
        Returns:
            Digraph: new Digraph from stream.
        
        Raises:
            ValueError: if the endpoints of any edge are not in prescribed range.
            ValueError: if the number of vertices or edges is negative.
            ValueError: if the input stream is in the wrong format.

        """
        V = stream.readInt()  # read the number of vertices
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        g = Digraph() if not vertex_type else Digraph(vertex_type)
        E = stream.readInt()  # read the number of edges
        if E < 0:
            raise ValueError("Number of edges in a Graph must be nonnegative")
        for _ in range(E):
            v = stream.readInt()  # read the first vertex,
            w = stream.readInt()  # read the second vertex,
            weight = stream.readFloat()
            g.add_edge(v, w, weight)
        return g
