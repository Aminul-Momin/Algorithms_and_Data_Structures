"""
Implementations of an symbol table with string keys using a R-way trie.

$ python3 TST.py data/shellsST.txt

    keys():
        by 	    4
        sea 	2
        sells 	1
        she 	0
        shells 	3
        shore 	6
        the 	5

    keys_with_prefix('sh'):
        she
        shells
        shore

    longest_prefix_of('shellsort'):
        shells

    keys_that_match('.he.l.'):
        shells

    keys_that_match('...'):
        sea
        she
        the
"""

from sys import argv


class TST(object):
    """An symbol table of key-value pairs, with string keys and generic values.

    A symbol table implements the associative array abstraction: when 
    associating a value with a key that is already in the symbol table, the
    convention is to replace the old value with the new value. Also the values
    associated with a key cannot be None —  setting the value None is equivalent
    to deleting the key from the symbol table. This implementation uses a ternary
    search trie.
    """
    def __init__(self):
        self.root = None  # Root of the TST
        self.n = 0  # size

    #*************************** Nested TST node: ****************************#

    class Node(object):
        """ Creates the inner Node class for the Sequential Search Symbol Table
        """
        def __init__(self, char=''):
            self.c = char  # Character
            self.value = None  # value associated with string
            self.left = None  # left subtree
            self.mid = None  # middle subtree
            self.right = None  # right subtree

    #************************ End of Nested TST node: ************************#

    def size(self):
        """ Return number of key-value pairs stored in this Symbol table.
        """
        return self.n

    def is_empty(self):
        """ Check whether this Symbol Table is empty or not
        """
        return self.n == 0

    def get(self, key):
        """ Return the value associate with the given key

        Args:
            key: the key of which value to be gotten
        Returns:
            value associated with the given key if the key is in the table or
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search None in the ST")
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.value

    def _get(self, x, key, i):
        """ Return the subtree associate with the given key

        Args:
            x  : the subtree
            key: the key with which a value is associated
            i  : the index of the string given as key
        Returns:
            subtree corresponding to the given key if the key is in the table
            or None if the key is not in the symbol table.
        """
        if x is None:
            return None
        if len(key) == 0:
            raise ValueError("Can't search empty string")
        if key[i] < x.c:
            return self._get(x.left, key, i)
        elif key[i] > x.c:
            return self._get(x.right, key, i)
        elif i < len(key) - 1:
            return self._get(x.mid, key, i + 1)
        else:
            return x

    def contains(self, key):
        """ Check whether this Symbol Table contains the given key or not

        Args:
            key: the key to check if it is in the table
        Returns:
            True if the table contains the given key or False otherwise
        """
        return self.get(key) != None

    def put(self, key, value):
        """ Inserts the key-value pair into the symbol table.

        It overwriting the old value with the new value if the key is already
        in the symbol table. If the value is None, this effectively deletes
        the key from the table.
        Args:
            key  : the key (string object)
            value: value associated with the given key
        """
        if key is None:
            raise ValueError("Cannot insert 'None' into the table")
        if not self.contains(key):
            self.n += 1
        self.root = self._put(self.root, key, value, 0)

    def _put(self, x, key, value, i):
        """ Add the given key-value pair in the subtree rooted at x.

        Args:
            x    : the subtree
            key  : the key (string object)
            value: value associated with the given key
            i    : index of the string given as key
        """
        if x is None:
            x = self.Node(key[i])

        if key[i] < x.c:
            x.left = self._put(x.left, key, value, i)  # if != elif
        elif key[i] > x.c:
            x.right = self._put(x.right, key, value, i)
        elif i < len(key) - 1:
            x.mid = self._put(x.mid, key, value, i + 1)
        else:
            x.value = value
        return x

    def longest_prefix_of(self, query):
        """ Return the string from the ST which is the longest prefix of the
        given query string, if no such string returns None.

        Args:
            query: the query string
        Returns:
            string that is the longest prefix of the given query string or
            None if no such string.
        """
        x = self.root
        i = 0
        length = 0

        while x is not None and i < len(query):
            if query[i] < x.c:
                x = x.left
            elif query[i] > x.c:
                x = x.right
            else:
                i += 1
                if x.value is not None:
                    length = i
                x = x.mid

        return query[:length]

    def keys(self):
        """ It collects and return all the keys in the symbol table.

        Returns:
            Iterable containing all the keys in the table
        """
        queue = []
        self._collect(self.root, '', queue)
        return queue

    def _collect(self, x, prefix, queue):
        """ It collects all keys with given prefix from subtrie rooted at x.

        Args:
            x     : the subtree
            prefix: the prefix of which we need to collect the keys with.
            queue : the queue which hold collected keys
        """
        if x is None:
            return
        self._collect(x.left, prefix, queue)
        if x.value is not None:
            queue.append(prefix + x.c)
        self._collect(x.mid, prefix + x.c, queue)
        self._collect(x.right, prefix, queue)

    def keys_with_prefix(self, prefix):
        """Return all of the keys from the ST that start with the given prefix.

        args:
            prefix: prefix of which we need to collect the keys start with.
        Returns:
            Iterable of all keys that starts with prefix
        """
        if prefix is None:
            raise ValueError("Can't collect 'None'")
        queue = []
        x = self._get(self.root, prefix, 0)
        if x is None:
            return queue
        if x.value is not None:
            queue.append(prefix)
        self._collect(x.mid, prefix, queue)
        return queue

    def keys_that_match(self, pattern):
        """ Collect the keys that match the given pattern.

        Returns all of the keys in the symbol table that match pattern,
        where '.' symbol is treated as a wildcard character.
        Args:
            pattern: pattern of which we need to collect keys matching with
        Returns:
            Iterable of all keys that matches with the given pattern
        """
        queue = []
        self._collect_match(self.root, pattern, queue, 0, '')
        return queue

    def _collect_match(self, x, pattern, q, i, prefix):
        """ It collects all keys from subtrie x that match with given pattern.

        Args:
            x      : the subtries
            pattern: pattern of which we need to collect keys matching with
            q      : queue which hold collected keys
            i      : index of the string given as pattern
            prefix : the prefix of the pattern
        """
        if x is None:
            return None
        if pattern[i] < x.c:
            self._collect_match(x.left, pattern, q, i, prefix)
        if pattern[i] == '.' or pattern[i] == x.c:
            if i == len(pattern) - 1 and x.value is not None:
                q.append(prefix + x.c)
            if i < len(pattern) - 1:
                self._collect_match(x.mid, pattern, q, i + 1, prefix + x.c)
        if pattern[i] > x.c:
            self._collect_match(x.right, pattern, q, i, prefix)

    def keys_that_match_plus(self, pattern):
        """ Collect the keys that match the given pattern.

        Returns all of the keys in the symbol table that match pattern,
        where '.' symbol is treated as a wildcard character.
        Args:
            pattern: pattern of which we need to collect keys matching with
        Returns:
            Iterable of all keys that matches with the given pattern
        """
        queue = []
        prefix = []
        self._collect_match_plus(self.root, pattern, queue, 0, prefix)
        return queue

    def _collect_match_plus(self, x, pattern, q, i, prefix):
        """ It collects all keys from subtrie x that match with given pattern.

        Args:
            x      : the subtries
            pattern: pattern of which we need to collect keys matching with
            q      : queue which hold collected keys
            i      : index of the string given as pattern
            prefix : the prefix of the pattern
        Notes:
            This procedures improve the time complexity of concatenation of
            the string 'prefix + x.c'
        """
        if x is None: return None
        c = pattern[i]
        if c < x.c: self._collect_match_plus(x.left, pattern, q, i, prefix)
        if c == '.' or c == x.c:
            prefix.append(x.c)
            if i == len(pattern) - 1 and x.value is not None:
                q.append(''.join(prefix))
            if i < len(pattern) - 1:
                self._collect_match_plus(x.mid, pattern, q, i + 1, prefix)
            prefix.pop(len(prefix) - 1)
        if c > x.c: self._collect_match_plus(x.right, pattern, q, i, prefix)

    #************************ Python Special Methods: ************************#

    def __len__(self):
        return self.size()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    #********************* End of Python Special Methods *********************#


def main():
    print(argv)


if __name__ == '__main__':
    if argv: print(argv)
    main()
