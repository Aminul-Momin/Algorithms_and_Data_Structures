"""
This module represents a data type called Suffix Array. This implementation
uses a private class Suffix to represent a suffix of a string (using constant
time and space) and list.sort() to sort the list of suffixes.
"""

from typing import List


class Suffix:
    def __init__(self, text: str, idx: int) -> None:
        self.text = text
        self.index = idx

    def __gt__(self, that) -> bool:
        return self.text > that.text


class SuffixArray:
    def __init__(self, text: str):
        self._n = len(text)
        self._suffixes: List[str] = []

        for i in range(self._n):
            self._suffixes.append(Suffix(text, i))
        self._suffixes.sort()

    def index(self, i: int) -> int:
        """Find the index into the original string of the ith smallest suffix.

        Args:
            i (int): Index of a suffix.

        Raises:
            IndexError: if the given index is out of bounds.

        Returns:
            The index into the original string of the ith smallest suffix.
        """
        if not (0 <= i < len(self._suffixes)):
            raise IndexError('invalid index !')
        return self._suffixes[i].index

    def lcp(self, i: int) -> int:
        """Computes the length of LCP of ith and (i-1)th smallest suffix.

        Args:
            i (int): an index between 0 and self._n.

        Raises:
            IndexError: if index out of bounds.

        Returns:
            The length of LCP of ith and (i-1)th smallest suffix.
        """
        if not (0 <= i < self._n):
            raise IndexError('invalid index !')
        return self.longest_common_prefix(self._suffixes[i],
                                          self._suffixes[i - 1])

    def longest_common_prefix(self, s: str, t: str) -> int:
        """Computes the length of LCP of two texts.

        Args:
            s (str): the first text.
            t (str): the second text.

        Returns:
            The length of LCP of two texts.
        """
        if not s or not t: return -1

        n = min(len(s), len(t))
        for i in range(n):
            if s[i] != t[i]: return i

    def __len__(self):
        return len(self._suffixes)
