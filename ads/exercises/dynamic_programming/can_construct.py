from typing import Iterable
'''
Write a function 'can_construct(target, word_bank)' that accepts a target string
and an aarray of strings.

The function should return a boolean indicating whether or not the 'target' can
be constructed by concatenating elements of the 'word_bank' array.

You may reuse elements of 'word_bank' as many times as needed.

Examples:
    1. can_construct(('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) -> True
    2. can_construct(('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) -> False
    3. can_construct(('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) -> True
    4. can_construct(('eeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) -> False
'''


def can_construct_rec(target: str, word_bank: Iterable) -> bool:
    """Find if it is possible to construct 'target' by concatenating elements .

    Args:
        target: The string to be constructed.
        word_bank: Collection of strings.

    Returns:
        whether or not the 'target' can be constructed by concatenating
        elements of the 'word_bank' array.
    """
    if target == '': return True

    for word in word_bank:
        if target.find(word) == 0:
            if can_construct_rec(target[len(word):], word_bank): return True

    return False


def can_construct_memo(target: str, word_bank: Iterable, memo={}) -> bool:
    """Find if it is possible to construct 'target' by concatenating elements .

    Args:
        target: The string to be constructed.
        word_bank: Collection of strings.

    Returns:
        whether or not the 'target' can be constructed by concatenating
        elements of the 'word_bank' array.
    """
    if target in memo: return memo[target]
    if not target: return True

    for word in word_bank:
        if target.find(word) == 0 and can_construct_memo(
                target[len(word):], word_bank):
            memo[target] = True
            return True

    memo[target] = False
    return False


def can_construct_tbl(target: str, word_bank: Iterable) -> bool:
    """Find if it is possible to construct 'target' by concatenating elements .

    Args:
        target: The string to be constructed.
        word_bank: Collection of strings.

    Returns:
        whether or not the 'target' can be constructed by concatenating
        elements of the 'word_bank' array.
    """
    tbl = [True] + [False] * len(target)

    for i in range(len(target)):
        if tbl[i] is True:
            for word in word_bank:
                if i + len(word) <= len(target) and target[i:i + len(word)] == word:
                    # if i+len(word) <= len(tbl):
                    tbl[i + len(word)] = True

    return tbl[len(target)]
