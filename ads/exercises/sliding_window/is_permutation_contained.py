from collections import Counter

def is_permutation(s1, s2):
    print(s1, s2)
    s1_counter = Counter(s1)
    k = len(s1)
    if k > len(s2)-1: return False
    
    for i in range(k, len(s2)+1):
        s2_counter = Counter(s2[i-k:i])
        if s1_counter == s2_counter: return True
    
    return False

def test_check_inclusion():
    test_cases = [
        ("ab", "eidbaooo", True),  # "ba" is a permutation of "ab"
        ("ab", "eidboaoo", False), # No permutation of "ab" in "eidboaoo"
        ("adc", "dcda", True),     # "dca" or "cad" is a permutation of "adc"
        ("hello", "ooolleoooleh", False), # No permutation of "hello" in "ooolleoooleh"
        ("a", "a", True),          # "a" is trivially a permutation of "a"
        ("abc", "bbbca", True),    # "bca" is a permutation of "abc"
        ("abc", "bbbab", False),   # No permutation of "abc" in "bbbab"
        ("", "anything", True),    # Empty string is trivially a permutation
        ("anything", "", False),   # Non-empty string cannot be found in an empty string
        ("xyz", "zyxwvutsrqponmlkjihgfedcba", True),  # "xyz" is a permutation of "zyx"
        ("aaa", "aaaaaa", True),   # "aaa" is trivially a permutation of "aaa"
        ("xyz", "axyzxyzxyz", True), # "xyz" is a permutation of itself, appearing multiple times
        ("longstring", "thisisaverylongstringexample", True), # "longstring" is a permutation of "longstring"
        ("short", "longstringexample", False), # No permutation of "short" in "longstringexample"
        ("123", "321", True),      # "321" is a permutation of "123"
    ]

    # Example usage to test the function
    for s1, s2, expected in test_cases:
        try:
            result1 = is_permutation(s1, s2)
            assert result1 == expected
        except AssertionError:
            print(f"check_inclusion('{s1}', '{s2}') = {result1}, expected: {expected}")
#=================================================================
# test_check_inclusion()

is_permutation('xyz', 'zyxwvutsrqponmlkjihgfedcba')
# is_permutation("adc", "dcda")
# is_permutation('ab', 'eidbaooo')
# is_permutation("ab", "eidbaooo")