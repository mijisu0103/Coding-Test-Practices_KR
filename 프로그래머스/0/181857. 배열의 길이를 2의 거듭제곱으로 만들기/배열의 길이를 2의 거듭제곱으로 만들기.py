def solution(arr):
    target = 1

    while target < len(arr):
        target *= 2

    return arr + [0] * (target - len(arr))