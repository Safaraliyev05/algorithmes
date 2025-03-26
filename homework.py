def func(arr):
    if len(arr) < 3:
        return False

    peak = 0
    n = len(arr)

    while peak + 1 < n and arr[peak] < arr[peak + 1]:
        peak += 1

    if peak == 0 or peak == n - 1:
        return False

    while peak + 1 < n and arr[peak] > arr[peak + 1]:
        peak += 1

    return peak == n - 1
