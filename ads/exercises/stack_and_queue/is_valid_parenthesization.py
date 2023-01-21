from random import randint
from ads.fundamentals import SLLNode, SLL
from ads.utils.utils import SLLNode, SLL
#==============================================================================


def is_well_formed(string):

    left_brackets, LOOKUP = [], {'(': ')', '{': '}', '[': ']'}
    for char in string:
        if char in LOOKUP: left_brackets.append(char)
        elif not left_brackets or char != LOOKUP[left_brackets.pop()]:
            # Unmatched right char or mismatched chars.
            return False

    return not left_brackets


def main():
    pass


if __name__ == '__main__':
    main()
