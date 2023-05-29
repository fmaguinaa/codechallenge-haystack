from random import random

from utils import order_even_odds

N = 100000
arr = [int(random() * N) for i in range(N)]
order_arr = order_even_odds(arr)
print("Before order even odds")
print(arr)
print("Ordered even odds")
print(order_arr)
