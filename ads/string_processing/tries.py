"""
Implementations of an symbol table with string keys using a R-way trie.


$ python3 tries.py data/shellsST.txt

    keys():
        by
        sea
        sells
        she
        shells
        shore
        the

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


class TriesST(object):
    """ An symbol table of key-value pairs, with string keys and generic values

    The TrieST class represents an symbol table of key-value pairs. A symbol
    table implements the associative array abstraction: when associating a
    value with a key that is already in the symbol table, the convention is to
    replace the old value with the new value. Also the values associated with
    a key cannot be 'None' —  setting the value None is equivalent to deleting
    the key from the symbol table. This implementation uses a 256-way trie.
    """

    #*************************** R-way trie node: ****************************#
    class Node(object):
        """Creates the inner Node class for the Sequential Search Symbol Table.
        """
        def __init__(self, value=None):
            self._value = value
            self._next = [None] * TriesST.R

    #************************ End of R-way trie node: ************************#

    R = 256  # extended ASCII alphabet size

    def __init__(self):
        self._root = None  # Root of the tries
        self._n = 0  # Number of keys in the tries

    def size(self):
        """Computes and returns the number of elements stored in this table.
        """
        return self._n

    def is_empty(self):
        """Check whether this Symbol Table is empty or not.
        """
        return self._n == 0

    def get(self, key):
        """Return the value associate with the given key.

        Args:
            key: the key of which value to be gotten

        Returns:
            value associated with the given key if the key is in the table and
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search 'None' in the ST")
        x = self._get(self._root, key, 0)
        if x is None:
            return None
        return x._value

    def _get(self, x, key, i):
        """ Return the subtree associate with the given key

        Args:
            x  : The subtree
            key: The key with which a value is associated
            i  : The index into the string given as key

        Returns:
            subtree corresponding to the given key if the key is in the table and
            None if the key is not in the symbol table.
        """
        if x is None:
            return None
        if i == len(key):
            return x
        else:
            return self._get(x._next[ord(key[i])], key, i + 1)

    def contains(self, key):
        """ Check whether this Symbol Table contains the given key or not

        Args:
            key: The key to check if it is in the table.

        Returns:
            True if the table contains the given key or False otherwise
        """
        if key is None:
            raise ValueError("Can't search 'None'")
        return self.get(key) is not None

    def put(self, key, value):
        """ Inserts the key-value pair into the symbol table.

        It overwrites the old value with the new value if the key is already
        in the symbol table. If the value is None, this effectively deletes
        the key from the table.

        Args:
            key  : the key given as string
            value: value associated with the given key
        """
        if key is None:
            raise ValueError("Cannot insert 'None' into the table")
        if value is None:
            self.delete(key)
        self._root = self._put(self._root, key, value, 0)

    def _put(self, x, key, value, i):
        """ Add the given key-value pair in the subtree rooted at x.

        Args:
            x    : the subtree
            key  : The key given as string
            value: Value associated with the given key
            i    : Index into the string given as key
        """
        if x is None:
            x = self.Node()
        if i == len(key):
            if x._value is None:
                self._n += 1
            x._value = value
            return x
        else:
            r = ord(key[i])
            x._next[r] = self._put(x._next[r], key, value, i + 1)
        return x

    def delete(self, key):
        """ Remove the given key if it is in the symbol table.

        Args:
            key: The key to be removed
        """
        if key is None:
            raise ValueError("Cant' detele None from the ST")
        self._root = self._delete(self._root, key, 0)

    def _delete(self, x, key, i):
        """ Remove the given key from the subtries rooted at x.

        Args:
            x  : The subtries
            key: The key to be removed
            i  : Index into the string given as key
        """
        if x is None:
            return None
        elif i == len(key):
            if x._value is not None:
                self._n -= 1
            x._value = None
        else:
            x._next[ord(key[i])] = self._delete(x._next[ord(key[i])], key,
                                                i + 1)

        if x._value is not None:
            return x

        # If the subtries rooted at x is completely expty, removes it
        for y in x._next:
            if y is not None:
                return x
        return None

    def longest_prefix_of(self, query):
        """ Compute the longest prefix of the given query.

        Return the string from the ST which is the longest prefix of the
        given query string, if no such string returns None.

        Args:
            query: The query string

        Returns:
            the string that is the longest prefix of the given query string or
            None if no such string.
        """
        if query is None:
            raise ValueError("'query' can't be 'None'")
        length = self._length(self._root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[:length]

    def _length(self, x, query, i, length):
        """ Compute the length of longest prefix of the given query.

        returns the length of the longest string key in the subtrie rooted
        at x that is a prefix of the query string, assuming the first d
        character match and we have already found a prefix match of given
        length (-1 if no such match)

        Args:
            x     : The subtries
            query : The query string
            i     : Index into  the query string
            lenght: Lenght of string that is so far longest prefix of query
        """
        if x is None:
            return length
        if x._value is not None:
            length = i
        if i == len(query):
            return length
        else:
            return self._length(x._next[ord(query[i])], query, i + 1, length)

    def keys(self):
        """ It collects and return all the keys in the symbol table.

        Returns:
            Iterable containing all the keys in the table
        """
        return self.keys_with_prefix('')

    def keys_with_prefix(self, prefix):
        """ Return all of the keys from the ST that start with the given prefix.

        args:
            prefix: Prefix of which we need to collect the keys start with.

        Returns:
            Iterable of all keys that starts with prefix

        Warning: It has not been implemented properly !!!
        """
        if prefix is None:
            raise ValueError("Prefix can't be 'None'")
        queue = []
        x = self._get(self._root, prefix, 0)
        if x is None:
            return queue
        prefix = list(prefix)
        self._collect(x, prefix, queue)
        return queue

    def _collect(self, x, a, queue):
        """ It collects all keys with given prefix from subtrie rooted at x.

        Args:
            x    : The subtree
            a    : The list of characters - prefix of query.
            queue: The queue which hold collected keys
        """
        if x is None:
            return
        if x._value is not None:
            queue.append(''.join(a))

        for i in range(TriesST.R):
            a.append(chr(i))
            self._collect(x._next[i], a, queue)
            a.pop()

    def keys_that_match(self, pattern):
        """ Collect the keys that match the given pattern.

        Returns all of the keys in the symbol table that match pattern,
        where '.' symbol is treated as a wildcard character.

        Args:
            pattern: Pattern of which we need to collect keys matching with

        Returns:
            Iterable of all keys that matches with the given pattern
        """
        queue = []
        prefix = []
        self._collect_match(self._root, pattern, prefix, queue)
        return queue

    def _collect_match(self, x, pattern, prefix, q):
        """ It collects all keys from subtrie x that match with given pattern.

        Args:
            x      : The subtries
            pattern: Pattern of which we need to collect keys matching with
            q      : Queue which hold collected keys
            i      : Index into the string given as pattern
            prefix : The prefix of the pattern
        """
        if x is None:
            return
        if len(prefix) == len(pattern):
            if x._value is not None:
                q.append(''.join(prefix))
            return

        char = pattern[len(prefix)]
        if char == '.':
            for i in range(TriesST.R):
                prefix.append(chr(i))
                self._collect_match(x._next[i], pattern, prefix, q)
                prefix.pop()
        else:
            prefix.append(char)
            self._collect_match(x._next[ord(char)], pattern, prefix, q)
            prefix.pop()

    #************************ Python Special Methods: ************************#
    def __len__(self):
        return self.size()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    def __delitem__(self, key):
        self.delete(key)

    #********************* End of Python Special Methods *********************#


## ============================================================================
## ============================================================================
def read_data_file(file_path, triesST):
    print("loading data ....")
    with open(file_path, encoding="utf-8") as f:  # Open the file
        while True:
            line = f.readline()
            if not line:
                break  # line is empty so exit
            for idx, word in enumerate(line.split()):
                triesST.put(word, idx)


def display(ST):
    print('\n' + "keys(): ")
    for key in ST.keys():
        print(f"\t{key}")

    print('\n' + "keys_with_prefix('sh'): ")
    for key in ST.keys_with_prefix('sh'):
        print('\t' + key)

    print('\n' + "longest_prefix_of('shellsort'): ")
    lp = ST.longest_prefix_of('shellsort')
    print('\t' + lp)

    print('\n' + "keys_that_match('.he.l.'): ")
    for key in ST.keys_that_match(".he.l."):
        print('\t' + key)

    print('\n' + "keys_that_match('...'): ")
    for key in ST.keys_that_match("..."):
        print('\t' + key)


def main(file_path=None):

    T1 = TriesST()

    if not file_path:
        shellsST = "she sells sea shells by the sea shore".split()
        for i, v in enumerate(shellsST):
            T1[v] = i
    else:
        read_data_file(file_path, T1)

    display(T1)


if __name__ == "__main__":
    import sys
    main(sys.argv[1]) if len(sys.argv) > 1 else main()
