"""
The module provides a 'union-find' data type also known as 'Disjoint Sets' data type.
"""


class DisjointSetsQF():
    """
    The class represents a 'Union-Find' data structures where 'find' operation
    is optimized to have constant time complexity.
    """
    def __init__(self, N):
        """Initializes an empty DisjointSetQU with 'N' elements 0 through "N'-1.

        Initially each element is in it's own component

        Args:
            N (int): the number of elements.
        """
        self.n = N  # Number of elements
        self.parent = [i for i in range(self.n)]  # parent[i] = parent of i

    def find(self, i):
        """Find the canonical element of the set containing element 'i'.

        Args:
            i (int): an element.

        Returns:
            int: the canonical element of the set containing element 'i'.
        """

    def union(self, x, y):
        """Merges the set containing element 'x' with the set containing element 'y'.

        Args:
            x (int): one element.
            y (int): the other element.
        """

    def is_connected(self, x, y):
        """Check if element 'x' and 'y' are connected or not.

        Args:
            x (int): one element
            y (int): the other element

        Returns:
            bool: True if 'x' an 'y' are in the same set False otherwise.
        """
        return self.find(x) == self.find(y)

    def count(self):
        """Count the number of total elements.

        Returns:
            int: the number of total elements.
        """
        return self.n


class DisjointSetsQU(DisjointSetsQF):
    """
    The class represents a 'Union-Find' data structures where 'union' operation
    is optimized to have constant time complexity.
    """
    def __init__(self, N):
        """Initializes an empty DisjointSetQU with 'N' elements 0 through "N'-1.

        Initially each element is in it's own component

        Args:
            N (int): the number of elements.
        """
        super(DisjointSetsQU, self).__init__(N)

    def union(self, x, y):
        """Merges the set containing element 'x' with the set containing element 'y'.

        Args:
            x (int): one element.
            y (int): the other element.
        """
        i = self.find(x)
        j = self.find(y)
        self.parent[i] = self.parent[j]

    def find(self, i):
        """Find the canonical element of the set containing element 'i'.

        Args:
            i (int): an element.

        Returns:
            int: the canonical element of the set containing element 'i'.
        """
        while i != self.parent[i]:
            i = self.parent[i]
        return i


class DisjointSetsWeightedQU(DisjointSetsQU):
    """
    The class represents a 'Union-Find' data structures where 'union' operation
    is optimized to have constant time complexity.
    """
    def __init__(self, N):
        """Initializes an empty DisjointSetQU with 'N' elements 0 through "N'-1.

        Initially each element is in it's own component

        Args:
            N (int): the number of elements.
        """
        super(DisjointSetsQU, self).__init__(N)

    def union(self, x, y):
        """Merges the set containing element 'x' with the set containing element 'y'.

        Args:
            x (int): one element.
            y (int): the other element.
        """
        pass

    def find(self, i):
        """Find the canonical element of the set containing element 'i'.

        Args:
            i (int): an element.

        Returns:
            int: the canonical element of the set containing element 'i'.
        """
        pass
