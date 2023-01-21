from typing import Sequence, Union, Container
from math import factorial
#==============================================================================
"""
Write a program which computes all size k subsets of {1, 2, ..., n} where
k and n are program inputs. - [EPI: 15.5].
"""


# print all subsets that take k of the remaining elements, with given prefix
def comb_str_v1(s: str, k: int) -> None:
    def _comb_str_v1(s: str, prefix: str, k: int) -> None:
        if k > len(s): return None
        elif k == 0: result.append(prefix)
        else:
            _comb_str_v1(s[1:], prefix + s[0], k - 1)
            _comb_str_v1(s[1:], prefix, k)

    result = []
    _comb_str_v1(s, "", k)
    return result


# print all subsets that take k of the remaining elements, with given prefix
def comb_str_v2(s: str, k: int) -> None:
    def _comb_str_v2(s: str, prefix: str, k: int) -> None:
        if k == 0: result.append(prefix)
        else:
            for i in range(len(s)):
                _comb_str_v2(s[i + 1:], prefix + s[i], k - 1)

    result = []
    _comb_str_v2(s, "", k)
    return result


def n_choose_k(n: int, k: int):
    def _n_choose_k(n: int, k: int, offset: int, result, chosen=[]):
        if len(chosen) == k: result.append(list(chosen))

        # Generate remaining combinations over {offset, ..., n - 1} of size
        remaining_to_choose = k - len(chosen)
        i = offset
        while i <= n and remaining_to_choose <= n - i + 1:
            chosen.append(i)
            _n_choose_k(n, k, i + 1, result, chosen)
            chosen.pop()
            i += 1

    result = []
    _n_choose_k(n, k, 1, result)
    return result


def comb_list_v1(L: Union[str, list], k: int) -> Container[Sequence]:
    def _comb_list_v1(L, k, start, result, chosen=[]):
        if (k == len(chosen)):
            result.append(''.join([str(i) for i in chosen]))
        else:
            i = start
            reamining_to_chose = k - len(chosen)
            while i <= len(L) and reamining_to_chose <= len(L) - i:
                chosen.append(L[i])
                _comb_list_v1(L, k, i + 1, result, chosen)
                chosen.pop()
                i += 1

    result = []
    _comb_list_v1(L, k, 0, result)
    return result


def comb_list_v2(L: Union[str, list], k: int) -> Container[Sequence]:
    def _comb_list_v2(L, k, start, result, chosen=[]):
        if (k == len(chosen)):
            result.append(''.join([str(i) for i in chosen]))
        else:
            for i in range(start, len(L) + 1):
                # k - len(chosen) -> reamining_to_chose
                if k - len(chosen) <= len(L) - i:
                    chosen.append(L[i])
                    _comb_list_v2(L, k, i + 1, result, chosen)
                    chosen.pop()

    result = []
    _comb_list_v2(L, k, 0, result)
    return result


def main():
    s = "RACE"
    k = 4
    comb1 = comb_str_v1(s, k)
    comb2 = comb_str_v2(s, k)
    assert comb1 == comb2
    print(comb1, comb2, sep='\n')
    print("*" * 40)

    L = list("TEA")
    n, k = len(L), 3

    n_chose_k = factorial(n) / (factorial(n - k) * factorial(k))
    print(f"""N: {n}; k: {k}; {n}-Chose-{k}: {n_chose_k}""")

    res1 = comb_list_v1(L, k)
    res2 = comb_list_v2(L, k)
    assert res1 == res2
    choose_k_from_n = n_choose_k(n, k)

    print(res1, res2, choose_k_from_n, sep='\n')


if __name__ == '__main__':
    main()
