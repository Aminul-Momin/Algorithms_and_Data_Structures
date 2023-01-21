"""
It is natural to apply graph models and algorithms to spatial problems. Consider a black and whitedigitized image of a maze-white pixels represent open €ueas and black spaces are walls. There aretwo special white pixels: one is designated the entrance and the other is the exit. The goal in thisproblem is to find a way of getting from the entrance to the exit, as illustrated in Figure 18.5 on thenext page.

Given a 2D array of black and white entries representing a maze with designated entrance and exit points, find a path from the entrance to the exit, if one exists.

Hint: Model the maze as a graph.
"""


def traverse(maze):
    def _mark_visited(i, j): maze[i][j] = 0

    def _is_unvisited_room(i, j): return maze[i][j] == 1

    def _is_within_bounds(i, j):
        return i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0])

    def _get_next_candidates(i, j):
        return filter(
            lambda c: _is_within_bounds(c[0], c[1]) and _is_unvisited_room(
                c[0], c[1]),
            [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)],
        )

    ENTRANCE = (0, 0)
    EXIT = (len(maze) - 1, len(maze[0]) - 1)

    progress = [([], ENTRANCE)]

    while progress:
        path, curr = progress.pop()

        if curr == EXIT: return True, path + [curr]
        progress.extend([(path + [curr], cand) for cand in _get_next_candidates(curr[0], curr[1])])

        _mark_visited(curr[0], curr[1])

    return False, []


def main():
    return all([
        traverse([
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 1],
        ]) == (True, [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]),
        traverse([
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
        ]) == (True, [
            (0, 0),
            (0, 1),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 3),
            (3, 2),
            (3, 1),
            (4, 1),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
        ]),
        traverse([
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
        ]) == (False, []),
    ])


if __name__ == '__main__':
    main()
