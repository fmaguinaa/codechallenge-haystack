def order_even_odds(arr):
    n = len(arr)
    i = 0
    j = 0
    k = n - 1
    while i < n and j < k:
        if arr[i] % 2:
            arr[i], arr[k] = arr[k], arr[i]  # O(1)
            k -= 1
            i -= 1
        else:
            j = i
        i += 1
    return arr
