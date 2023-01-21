"""
Write a program that takes an array denoting the daily stock price, and
returns the maximum profit that could be made by buying and then selling one
share of that stock. - [EPI: 5.6].
"""
#==============================================================================


def buy_sell_once(prices):

    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


def buy_sell_once_v2(prices):
    max_profit, lowest = 0, float('inf')

    for price in prices:
        lowest = min(lowest, price)
        max_profit = max(max_profit, price - lowest)
    return max_profit
