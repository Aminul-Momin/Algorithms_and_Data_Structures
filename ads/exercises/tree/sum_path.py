def sum_path(x, sum):
    def _sum_path(x, sum, paths, path=[]):
        if x is None:
            return
        path.append(x._key)
        sum = sum - x._key
        if sum == 0:
            paths.append(" -> ".join([str(i) for i in path]))
        _sum_path(x._left, sum, paths, path)
        _sum_path(x._right, sum, paths, path)
        path.pop()

    paths = []
    _sum_path(x, sum, paths)
    return paths


def _test_sum_path():
    def _find_path(x, key, path=[]):
        if x is None:
            raise ValueError("The specified key is not in the tree.")
        path.append(x._key)
        if key < x._key:
            return _find_path(x._left, key, path)
        elif key > x._key:
            return _find_path(x._right, key, path)
        else:
            return path

    L = [randint(0, 999) for _ in range(20)]
    bst = gen_bst(L)
    key = choice(L)
    path = _find_path(bst._root, key)
    _sum = sum(path)
    print(path, "\nSum: ", _sum, '\n', bst._root)

    print(sum_path(bst._root, _sum))
