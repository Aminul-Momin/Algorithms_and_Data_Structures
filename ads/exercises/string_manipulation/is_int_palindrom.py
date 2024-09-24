
def is_int_palindrome(n):
    """
    Checks if a given integer is a palindrome.

    Args:
        n: The integer to check.

    Returns:
        True if n is a palindrome, False otherwise.
    """

    if n < 0:
        return False  # Negative numbers cannot be palindromes

    divisor = 1
    while n // divisor >= 10:
        divisor *= 10

    while n != 0:
        left = n // divisor
        right = n % 10

        if left != right:
            return False

        n = (n % divisor) // 10
        divisor //= 100

    return True

# ============================================================================
def test_is_int_palindrom():
    test_cases = [
        (0, True),
        (-1, False),
        (-111, False),
        (122221, True),
        (123454321, True),
        (1234321, True),
    ]
    
    for test_case, expected in test_cases:
        returned = is_int_palindrome(test_case)
        
        try:
            assert returned == expected
        except AssertionError as ae:
            
            print(returned, expected)
# ============================================================================

if __name__ == '__main__':
    test_is_int_palindrom()