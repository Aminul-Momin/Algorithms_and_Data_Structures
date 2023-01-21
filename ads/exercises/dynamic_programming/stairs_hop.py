#==============================================================================
"""
You'r clambing stairs. You can advance 1 to k steps at a time. Your destination
is exactly n steps up.

Write a function `stairs_hop_k(m, n)` which takes inputs `n` (number of stairs)
and `k` (number of maximum hop) and returns the number of ways in which you can
get to your destination. - [CtCI:9.1, EPI:16.10].

NOTE:
    - if you can advance 3 steps (in oppose to k-steps) at most at a time

"""
#==============================================================================

from functools import lru_cache

@ lru_cache(None)
def stairs_3hop_rec(n):
    """
    Computes the number of ways to get to n steps up taking at most 3 steps.
    Args:
        n: number of stairs
    Returns:
        (int): the number of ways in which you can get to n steps up.
    """
    if n < 1: return 0
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return stairs_3hop_rec(n - 1)  \
         + stairs_3hop_rec( n - 2) \
         + stairs_3hop_rec(n - 3)


@ lru_cache(None)
def stairs_khop_rec(n: int, k: int = 3):
    if n <= 1: return 1
    return sum(stairs_khop_rec(n - i, k) for i in range(1, min(k, n) + 1))


def stairs_khop_memo(n: int, k: int = 3, memo={}):
    if n <= 0 or k <= 0: return 0
    
    def _stairs_khop_memo(n: int, k: int = 3, memo={}):
        """
        Computes the number of ways to get to n steps up taking at most `k` steps.
        
        Args:
            n: number of stairs
            k: number of maximum steps
        Returns:
            (int): the number of ways in which you can get to n steps up.
        """
        if n in memo: return memo[n]
        if n <= 1: return 1
        res = 0
        for i in range(1, min(k, n) + 1):
            res += _stairs_khop_memo(n - i, k, memo)
        memo[n] = res
        return memo[n]

    return _stairs_khop_memo(n, k, memo)

def stairs_khop_memo_v1(n, k):
    # ks = [0]*(k+1)
    # for i in range(1, len(ks)): ks[i] = sum(ks[:i])+1
    # if n <= k: return ks[n]
    # memo = {}
    # for i in range(k+1): memo[i] = ks[i]

    memo = {0: 0}
    for i in range(1, k + 1):
        memo[i] = sum(memo.values()) + 1

    def _stairs_khop_memo(n, k, memo):
        if n in memo: return memo[n]
        memo[n] = sum(
            _stairs_khop_memo(n - i, k, memo) for i in range(1, k + 1))
        return memo[n]

    return _stairs_khop_memo(n, k, memo)


def stairs_khop_memo_v2(n: int, k: int = 3, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return 1
    memo[n] = sum(stairs_khop_memo_v2(n-i, k, memo) for i in range(1, min(k, n) + 1))
    return memo[n]


def stairs_khop_memo_v3(n, k):
    def _stairs_khop_memo_v3(n, k, memo):
        if memo[n] > 0: return memo[n]
        if n <= 1: return 1
        for i in range(1, k + 1):
            if n - i >= 0:
                memo[n] += _stairs_khop_memo_v3(n - i, k, memo)
        return memo[n]

    memo = [0] * (n + 1)
    return _stairs_khop_memo_v3(n, k, memo)


def stairs_khop_tbl(n, k):
    ks = [0] * (k + 1)
    for i in range(1, len(ks)):
        ks[i] = sum(ks[:i]) + 1
    if n <= k: return ks[n]
    tbl = ks + [0] * (n - k)
    for i in range(k + 1, n + 1):
        tbl[i] = sum(tbl[i - j] for j in range(1, k + 1))
    return tbl[n]


def stairs_3hop_tbl(n):
    # memo = {1: 1, 2: 2, 3: 4}
    memo = [0, 1, 2, 4] + [0] * (n - 3)
    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


def stairs_3hop_tbl_2(n):
    def _stairs_3hop_tbl_2(n, result):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif result[n] == -1:
            temp3 = _stairs_3hop_tbl_2(n - 3, result)
            temp2 = _stairs_3hop_tbl_2(n - 2, result)
            temp1 = _stairs_3hop_tbl_2(n - 1, result)
            result[n] = temp1 + temp2 + temp3

        return result[n]

    result = [-1] * (n + 1)
    return _stairs_3hop_tbl_2(n, result)



def main():
    stairs_3hop = [stairs_3hop_rec, stairs_3hop_tbl, stairs_3hop_tbl_2]
    stairs_khop = [
        stairs_khop_rec, stairs_khop_memo, stairs_khop_memo_v2,
        stairs_khop_memo_v3, stairs_khop_memo_v1, stairs_khop_tbl
    ]
    for n in range(1, 10):
        for k in range(1, 10):
            if k == 3:
                result = stairs_3hop[0](n)
                for func in stairs_3hop:
                    assert result == func(n)
            else:
                result = stairs_khop[0](n, k)
                for func in stairs_khop:
                    if func == stairs_khop[1] or func == stairs_khop[2]:
                        assert result == func(n, k, {})
                    else:
                        assert func(n, k)

def _test_stairs_hop():
    # for n in range(1, 10):
    #     for k in range(1, 10):
    #         returned = stairs_khop_memo(n, k, memo={})
    #         print(returned)
    returned = stairs_khop_memo(5, 4, memo={})


if __name__ == '__main__':
    # main()
    _test_stairs_hop()
