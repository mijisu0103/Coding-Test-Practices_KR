def solution(arr, idx):
    answer = 0
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
        elif arr[i] == 0:
            continue
    return -1
        