import time
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

coins = [50, 25, 10, 5, 2, 1]
money = 163

# Вимірюємо час для жадібного алгоритму
start_time = time.time()
coins_greedy = find_coins_greedy(money, coins)
end_time = time.time()
print("Жадібний алгоритм (find_coins_greedy):")
print(coins_greedy)
print(f"Час виконання: {end_time - start_time:.6f} секунд\n")

# Вимірюємо час для алгоритму динамічного програмування
start_time = time.time()
min_coins = find_min_coins(money, coins)
end_time = time.time()
print("Алгоритм динамічного програмування (find_min_coins):")
print(min_coins)
print(f"Час виконання: {end_time - start_time:.6f} секунд")
