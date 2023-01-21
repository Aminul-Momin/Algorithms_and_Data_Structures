from random import randrange
from typing import Container
#==============================================================================
""" You have d dice, and each die has f faces numbered 1, 2, ..., f. Return all
the possible ways (out of f^d total ways) to roll the dice so the sum of the face
up numbers equals target. - [LeetCode: 1155]. """


def sum_dice_roll(dice: int, target: int, face=6) -> list:
    def _sum_dice_roll(N: int,
                       t: int,
                       face: int,
                       L: list,
                       _sum: int,
                       chosen=[]):
        if N == 0:
            if _sum == t:
                L.append(tuple(chosen))
        else:
            for i in range(1, face + 1):
                # (x < y < z) -> (y > x and y < z)
                if _sum + i + 1 * (N - 1) <= t <= _sum + i + 6 * (N - 1):
                    chosen.append(i)
                    _sum_dice_roll(N - 1, t, face, L, _sum + i, chosen)
                    chosen.pop()

    res = []
    _sum_dice_roll(dice, target, face, res, 0)
    for i in res:
        print(i)
    return res


def sum_dice_roll_alt(dice: int, target: int) -> list:
    def _sum_dice_roll_alt(N: int, t: int, L: list, _sum=0, chosen=[]) -> None:
        if N == 0:
            if t == _sum:
                L.append(tuple(chosen))
        else:
            for i in range(1, 7):
                if _sum + i + 1 * (N - 1) <= t and t <= _sum + i + 6 * (N - 1):
                    _sum_dice_roll_alt(N - 1, t, L, _sum + i, chosen + [i])

    combinations = []
    _sum_dice_roll_alt(dice, target, combinations)
    # for comb in combinations: print(comb)
    return combinations


def sum_dice_roll2(dice: int, target: int) -> Container[str]:
    def _sum_dice_roll2(n: int, t: int, L: Container[str], chosen=[]) -> None:
        if n == 0:
            if t == 0:
                L.append(tuple(chosen))
        else:
            for i in range(1, 7):
                if t - i >= 1 * (n - 1) and t - i <= 6 * (n - 1):
                    chosen.append(i)
                    _sum_dice_roll2(n - 1, t - i, L, chosen)
                    chosen.pop()

    combinations = []
    _sum_dice_roll2(dice, target, combinations)
    for comb in combinations:
        print(comb)
    return combinations


def main():
    dice = randrange(1, 5)
    target = randrange(1, 1 + dice * 6)

    res1 = sum_dice_roll(dice, target)
    res2 = sum_dice_roll_alt(dice, target)
    res3 = sum_dice_roll2(dice, target)
    assert res1 == res2 == res3
    print('Number of Dice: ', dice, 'Target: ', target)


if __name__ == '__main__':
    main()
