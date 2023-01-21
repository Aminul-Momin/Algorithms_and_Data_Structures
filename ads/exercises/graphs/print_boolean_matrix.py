"""
Implement a routine that takes an n x m Boolean array A together with an entry (x,y) and flips the color of the region associated with (x,y).

Hint: Solve this conceptually, then think about implementation optimizations.
"""


def flip_region(Ab, i, j):
    def neighbors(Ab, i, j):
        if i > 0:
            yield (i - 1, j)
        if i < len(Ab) - 1:
            yield (i + 1, j)
        if j > 0:
            yield (i, j - 1)
        if j < len(Ab[0]) - 1:
            yield (i, j + 1)

    _Ab = Ab
    target = not _Ab[i][j]
    visit_queue = [(i, j)]
    while visit_queue:
        _i, _j = visit_queue.pop(0)
        curr = _Ab[_i][_j]
        if curr == target:
            continue
        for n in neighbors(_Ab, _i, _j):
            _Ab[_i][_j] = target
            visit_queue.append(n)
    return _Ab


all([
    flip_region([
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
    ], 0, 2) == [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ],
])