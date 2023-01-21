from random import randint
from typing import List


def three_sum(L: List[int]) -> List[int]:

    L = sorted(L)
    res = []

    for i, val in enumerate(L):
        if i > 0 and val == L[i - 1]: continue
        low = i + 1
        high = len(L) - 1

        while low < high:
            three_sum = L[low] + L[high] + val
            if three_sum < 0: low += 1
            elif three_sum > 0: high -= 1
            else:
                res.append([val, L[low], L[high]])
                low += 1
                while L[low] == L[low - 1]:
                    low += 1
    return res


def main():
    for _ in range(10):

        L = [randint(-10, 10) for _ in range(15)]
        result = three_sum(L)
        print(result)


if __name__ == '__main__':
    main()
