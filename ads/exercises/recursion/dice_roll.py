from random import randrange
from typing import Container
#==============================================================================
""" 
Write a recursive function diceRoll that accepts an integer, number of six
sided dice to roll, and output all possible combinations of values that could
appear on the dice.
"""


def dice_roll(n: int) -> Container[str]:
    def _dice_roll(n: int, L: Container[str], chosen=[]) -> None:
        if n == 0:
            L.append(', '.join([str(i) for i in chosen]))
        else:
            for side in range(1, 7):
                _dice_roll(n - 1, L, chosen + [side])

    combinations = []
    _dice_roll(n, combinations)
    for comb in combinations:
        print(comb)
    return combinations


def main():
    n = randrange(0, 5)
    dice_roll(n)
    print('Number of Dice: ', n)


if __name__ == '__main__':
    main()
