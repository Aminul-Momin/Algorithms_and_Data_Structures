"""
Design an algorithm that takes as input an array and a number, and determines if there are three entries in the array (not necessarily distinct) which add up to the specified number. For example, if the array is <11,2,5,7,3> then there are three entries in the array which add up to 21 (3, 7, 11, and 5, 5, 11) (note that we can use 5 twice, since the problem statement said we c an use the same entry more than once). However, no three entries add up to 22.

Hint: How would you check if a given array entry can be added to two more entries to get the specified number?
"""


def has_three_sum(A, v):
    for a in A:
        j = 0
        k = len(A) - 1
        while j < k:
            _v = a + A[j] + A[k]
            if _v < v:
                j += 1
            elif _v > v:
                k -= 1
            else:
                return True
    return False

def has_three_sum(A, target):
    for item in A:
        left, right = 0, len(A) - 1
        
        while left < right:
            total = item + A[left] + A[right]
            if total < target: left += 1
            elif total > target: right -= 1
            else: return True
    
    return False

def main():
    return all([
        has_three_sum([11, 2, 5, 7, 3], 21),
        not has_three_sum([11, 2, 5, 7, 3], 100),
        not has_three_sum([11, 2, 5, 7, 3], 0),
    ])


if __name__ == '__main__':
    main()
