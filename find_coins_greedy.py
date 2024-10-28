def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
      count = amount // coin
      if count > 0:
        result[coin] = count

      amount = amount - (coin * count)

    return result