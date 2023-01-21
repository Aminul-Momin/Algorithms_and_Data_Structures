from typing import Sequence, Container, List

from ads.utils import *
#==============================================================================
""" Write a method to compute all permutations of a string. [CtCI: 9.5]. """


def permute_str_v1(s: str) -> Container[Sequence]:
    """
    Args:
        s: The string to be permuted.
    """
    def _permute_str_v1(prefix: str, sufix: str, result: list) -> None:
        if sufix == '': result.append(prefix)
        else:
            for i in range(len(sufix)):
                _permute_str_v1(prefix + sufix[i], sufix[:i] + sufix[i + 1:],
                                result)

    result = []
    _permute_str_v1('', s, result)
    return result


def permute_str_v2(s: str) -> Container[Sequence]:
    def _permute_str_v2(L: list, result: list, offset=0) -> None:
        if offset == len(L): result.append(''.join([str(i) for i in L]))
        else:
            for i in range(offset, len(L)):
                swap(L, offset, i)
                _permute_str_v2(L, result, offset + 1)
                swap(L, offset, i)

    result = []
    _permute_str_v2(list(s), result)
    return result


def permute_str_v3(s: str) -> Container[Sequence]:
    def _permute_str_v3(L: list, result: list, offset) -> None:
        if offset == 0: result.append(''.join([str(i) for i in L]))
        else:
            for i in range(0, offset + 1):
                swap(L, offset, i)
                _permute_str_v3(L, result, offset - 1)
                swap(L, offset, i)

    result = []
    L = list(s)
    offset = len(L) - 1
    _permute_str_v3(L, result, offset)
    return result


''' Permutation of list.  - [EPI: 15.3].

Write a program which takes as input an array of distinct integers and g
enerates all permutations of that array. No permutation of the array may
appear more than once.
'''


def permute_list_v1(L: List[chr]) -> Container[Sequence]:
    def _permute_list_v1(L: List[int], result: Container, chosen=[]) -> None:
        if len(L) == 0: result.append(''.join([str(i) for i in chosen]))
        else:
            for i in range(len(L)):
                first = L.pop(i)
                chosen.append(first)
                _permute_list_v1(L, result, chosen)

                L.insert(i, first)
                chosen.pop()

    result = []
    _permute_list_v1(L, result)
    return result


def permute_list_v2(L: List[chr]) -> Container[Sequence]:
    def _permute_list_v2(L, result, offset=0) -> None:
        if offset == len(L): result.append(''.join(L))
        else:
            for i in range(offset, len(L)):
                swap(L, offset, i)
                _permute_list_v2(L, result, offset + 1)
                swap(L, offset, i)

    result = []
    _permute_list_v2(L, result)
    return result


def permute_list_v3(L: List[chr]) -> Container[Sequence]:
    def _permute_list_v3(L, result, offset) -> None:
        if offset == 0: result.append(''.join(L))
        else:
            for i in reversed(range(offset + 1)):
                swap(L, offset, i)
                _permute_list_v3(L, result, offset - 1)
                swap(L, offset, i)

    result = []
    offset = len(L) - 1
    _permute_list_v3(L, result, offset)
    return result


def main():
    s = "RACE"
    comb1 = permute_str_v1(s)
    comb2 = permute_list_v1(list(s))
    print(comb1)
    assert comb1 == comb2


if __name__ == '__main__':
    main()
