from typing import List
from random import randint, sample
#==============================================================================
""" Coin Change

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
Example 2:
    Input: coins = [2], amount = 3
    Output: -1
Example 3:
    Input: coins = [1], amount = 0
    Output: 0
Example 4:
    Input: coins = [1], amount = 1
    Output: 1
Example 5:
    Input: coins = [1], amount = 2
    Output: 2
 

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
"""


def coin_change(amount: int, coins: List[int]) -> int:
    tbl = [amount + 1] * (amount + 1)
    tbl[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0: tbl[i] = min(tbl[i], 1 + tbl[i - coin])
    return tbl[amount] if tbl[amount] != amount + 1 else -1


def coin_change_v2(amount, coins):
    tbl = [amount + 1] * (amount + 1)
    tbl[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i + coin <= amount:
                tbl[i + coin] = min(1 + tbl[i], tbl[i + coin])
    return tbl[amount] if tbl[amount] != amount + 1 else -1


def min_change(amount, coins):
    def _min_change(amount, coins, memo):
        if amount in memo: return memo[amount]
        if amount == 0: return 0
        if amount < 0: return float('inf')
        min_coins = float('inf')

        for coin in coins:
            num_coins = 1 + _min_change(amount - coin, coins, memo)
            min_coins = min(min_coins, num_coins)

        memo[amount] = min_coins
        return min_coins

    ans = _min_change(amount, coins, {})
    if ans == float('inf'): return -1
    else: return ans


def _test_num_score_comb():
    target = randint(10, 30)
    L = sample(range(1, 10), 6)
    # target = 12
    # L = [2, 3, 7]
    res1 = coin_change(target, L)
    res2 = coin_change_v2(target, L)
    assert res1 == res2

    print(target, L)
    print(res1, res2)


if __name__ == '__main__':
    _test_num_score_comb()
