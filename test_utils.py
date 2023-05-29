from utils import order_even_odds
from random import random


def test_order_even_odds():
    arr = [1, 2, 3, 4, 5]
    assert order_even_odds(arr) == [4, 2, 3, 5, 1]


def test_order_only_even():
    arr = [2, 4, 6, 8, 10]
    assert order_even_odds(arr) == arr


def test_order_only_odd():
    arr = [1, 3, 5, 7, 9]
    assert order_even_odds(arr) == arr


def test_order_long_arr():
    n = 10000
    arr = [int(random() * n) for i in range(n)]
    ordered_arr = order_even_odds(arr)
    assert ordered_arr[0] % 2 == 0
    assert ordered_arr[-1] % 2 == 1
