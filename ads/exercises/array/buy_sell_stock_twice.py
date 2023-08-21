"""
Write a program that computes the maximum profit that can be made by buying
and selling a share at most twice. The second buy must be made on another
date after the first sale. - [EPI:5.7] .
"""
#==============================================================================


def buy_sell_twice(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day.

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit


def buy_sell_twice_v2(prices):

    max_total_profit, min_price_so_far = 0.0, prices[0]
    first_buy_sell_profits = [0.0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the second buy on that day.
    max_price_so_far = prices[-1]
    for i, price in reversed(list(enumerate(prices[1:], 1))):

        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i-1]
        )
        max_price_so_far = max(max_price_so_far, price)    
    
    return max_total_profit
