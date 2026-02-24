def solution(arr):
    if 2 not in arr:
        return [-1]
    
    start = arr.index(2)
    end = len(arr) - arr[::-1].index(2)
    
    return arr[start:end]