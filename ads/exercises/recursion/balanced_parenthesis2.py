
"""
LeetCode: 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
"""


"""
Approach 1: Brute Force


Intuition:
We can generate all 2^{2n} sequences of '(' and ')' characters. Then, we will
check if each one is valid.

Algorithm:
To generate all sequences, we use a recursion. All sequences of length n is
just '(' plus all sequences of length n-1, and then ')' plus all sequences of
length n-1.

To check whether a sequence is valid, we keep track of balance, the net
number of opening brackets minus closing brackets. If it falls below zero at
any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.

Complexity Analysis

Time Complexity : O(2^{2n}n). For each of 2^{2n} sequences, we need to create
and validate the sequence, which takes O(n) work.

Space Complexity : O(2^{2n}n). Naively, every sequence could be valid.
See Approach 3 for development of a tighter asymptotic bound.

"""


class GenParenthesis(object):
    def generateParenthesis(self, n):
        def generate(A=[]):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate()
        return ans

"""
Approach 2: Backtracking
Intuition and Algorithm

Instead of adding '(' or ')' every time as in Approach 1, let's only add them
when we know it will remain a valid sequence. We can do this by keeping track
of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place.
And we can start a closing bracket if it would not exceed the number of opening
brackets.
"""


def generateParenthesis( N):
    ans = []

    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans


"""
Approach 3: Closure Number
Intuition:

To enumerate something, generally we would like to express it as a sum of
disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence S: the least
index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. Clearly, every
parentheses sequence has a unique closure number. We can try to enumerate
them individually.

Algorithm:

For each closure number c, we know the starting and ending brackets must be
at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid
sequence, plus the rest of the elements must be a valid sequence.


Complexity Analysis:

Time and Space Complexity : O(4^n/sqrt(n)). The analysis is similar to Approach 2.

"""

def generateParenthesis2(self, N):
    if N == 0:
        return ['']
    ans = []
    for c in range(N):
        for left in self.generateParenthesis2(c):
            for right in self.generateParenthesis2(N-1-c):
                ans.append('({}){}'.format(left, right))
    return ans
