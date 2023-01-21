'''
Write a function 'count_construct(target, word_bank)' that accepts a target 
string and an aarray of strings.

The function should return the number of ways that the 'target' can be 
constructed by concatenating elements of the 'word_bank' array.

You may reuse elements of 'word_bank' as many times as needed.

Examples:
    1. count_construct(('', ['purp', 'p', 'ur', 'le', 'purpl'])) -> 1
    2. count_construct(('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) -> 2
    3. count_construct(('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) -> 1
    4. count_construct(('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) -> 0
    5. count_construct(('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) -> 4
    6. count_construct(('eeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeee'])) -> 0
'''


def count_construct_rec(target, word_bank):
    """Counts the number of ways that 'target' can be constructed.

    Args:
        target (str): The string to be constructed.
        word_bank (Iterable[str]): Collection of string from which 'target'
            can be constructed.

    Returns:
        int: The number of ways that the 'target' can be constructed by
            concatenating elements of the 'word_bank' array.
    """
    if target == '': return 1
    total_count = 0

    for word in word_bank:
        if target.find(word) == 0:
            num_ways_rest = count_construct_rec(target[len(word):], word_bank)
            total_count += num_ways_rest

    return total_count

def count_construct_memo(target, word_bank, memo={}):
    """Counts the number of ways that 'target' can be constructed.

    Args:
        target (str): The string to be constructed.
        word_bank (Iterable[str]): Collection of string from which 'target'
            can be constructed.

    Returns:
        int: The number of ways that the 'target' can be constructed by
            concatenating elements of the 'word_bank' array.
    """
    if target in memo: return memo[target]
    if target == '': return 1
    total_count = 0

    for word in word_bank:
        if target.find(word) == 0:
            total_count += count_construct_memo(target[len(word):], word_bank)

    memo[target] = total_count
    return total_count


def count_construct_tbl(target, word_bank):
    """Counts the number of ways that 'target' can be constructed.

    Args:
        target (str): The string to be constructed.
        word_bank (Iterable[str]): Collection of string from which 'target'
            can be constructed.

    Returns:
        int: The number of ways that the 'target' can be constructed by
            concatenating elements of the 'word_bank' array.
    """

    tbl = [1]+[0]*len(target)

    for i in range(len(target)):
        for word in word_bank:
            if i+len(word) <= len(target) and target[i:i+len(word)] == word:
                tbl[i+len(word)] += tbl[i]

    return tbl[len(target)]
