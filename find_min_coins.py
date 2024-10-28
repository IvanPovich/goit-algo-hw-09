def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    last_coin = [-1] * (amount + 1)

    for coin in coins:
        for a in range(coin, amount + 1):
            if dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                last_coin[a] = coin

    result = {}

    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin == -1:
            return {}
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1

        current_amount -= coin

    return result