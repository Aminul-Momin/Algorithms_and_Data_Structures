"""
Consider a matrix of black and white entries. - [EPI: 18.03]

We say that an element in a 2D matrix is “enclosed” if there is no path from
any of them to the boundary that only passes through elements of the same color.

Write a program that takes a 2D array A, whose entries are either white or black,
and replaces all white elements that cannot reach the boundary with black.
"""


def compute_enclosed(A):
    def _is_within_bounds(i, j):
        return i >= 0 and i < len(A) and j >= 0 and j < len(A[0])

    def _is_edge(i, j):
        return i == 0 or i == len(A) - 1 or j == 0 or j == len(A[0]) - 1

    def _is_white(i, j):
        return A[i][j] == 1

    def _get_next_candidates(i, j):
        return filter(
            lambda c: _is_within_bounds(c[0], c[1]) and _is_white(c[0], c[1]),
            [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)],
        )

    def _clear(path):
        _path = path

        while _path:
            i, j = _path.pop()
            A[i][j] = 0
            _path.extend(_get_next_candidates(i, j))

    for i in range(len(A)):
        for j in range(len(A[0])):
            if not _is_white(i, j):
                continue

            path = [(i, j)]

            cleared = False
            while path and not cleared:
                _i, _j = path[-1]

                if _is_edge(_i, _j):
                    _clear(path)
                    cleared = True
                    continue

                cands = _get_next_candidates(_i, _j)
                if not cands:
                    cleared = True
                    continue

                path.extend(cands)

    return A