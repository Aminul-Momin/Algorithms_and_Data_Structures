from typing import Container, Sequence, List
#==============================================================================
"""
Write a function that takes as input a set and returns its power set. 
Alternatively, Given a collection of integers that might contain duplicates,
nums, return all possible subsets (the power set). - [EPI: 15.4].
"""


def power_set_list_v1(L: List[chr]) -> Container[Sequence]:
    """ Computes the power set of the given set, L."""
    def _power_set_list_v1(chose_from, result, chosen=[]):
        """
        Args:
            chosen    : list of chosen elements.
            chose_from: list of elements to chose from.
            result    : list of power set elements.
        """
        if len(chose_from) == 0:
            result.append(list(chosen))
        else:
            first = chose_from.pop(0)
            chosen.append(first)
            _power_set_list_v1(chose_from, result, chosen)

            chosen.pop()
            _power_set_list_v1(chose_from, result, chosen)

            chose_from.insert(0, first)

    result = []
    _power_set_list_v1(L, result)
    return result


# print all subsets of the characters in s
def power_set_str_v2(s: str) -> Container[Sequence]:
    """
        Note: it doesn't take empty set into accout. 
    """

    # print all subsets of the remaining elements, with given prefix
    def _power_set_str_v2(prefix: str, s: str, result) -> None:
        if len(s) > 0:
            # print(prefix+s[0])
            # result.append(prefix+s[0])
            result.append(prefix + s[0])
            _power_set_str_v2(prefix + s[0], s[1:], result)
            _power_set_str_v2(prefix, s[1:], result)

    res = []
    _power_set_str_v2("", s, res)
    return res


def power_set_str_v3(s: str) -> Container[Sequence]:
    def _power_set_str_v3(prefix: str, s: str, result) -> None:
        # print(prefix)
        result.append(prefix)
        for i in range(len(s)):
            _power_set_str_v3(prefix + s[i], s[i + 1:], result)

    res = []
    _power_set_str_v3("", s, res)
    return res


def main():
    s = "RACE"
    L: list[str] = list(s)
    ps1 = power_set_list_v1(L)
    ps2 = power_set_str_v2(s)  # it doesn't take empty set into accout.
    ps3 = power_set_str_v3(s)

    # assert len(ps1) == len(ps2) == pow(2, len(L))
    # assert len(ps1) == len(ps1)-1 == pow(2, len(L))-1

    print(ps1, ps2, ps3, sep='\n')


if __name__ == '__main__':
    main()
