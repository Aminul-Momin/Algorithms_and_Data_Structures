def buy_and_sell_k_times(prices, k):

    if not k:
        return 0.0
    elif 2 * k >= len(prices):
        temp1 = [max(0, b - a) for a, b in zip(prices[:-1], prices[1:])]
        return sum(temp1)

    min_price, max_profits = [float('inf')] * k, [0] * k

    for price in prices:
        for i in reversed(list(range(k))):
            max_profits[i] = max(max_profits[i], price - min_price[i])
            x = 0 if i == 0 else max_profits[i - 1]
            min_price[i] = min(min_price[i], price - x)

    return max_profits[-1]
