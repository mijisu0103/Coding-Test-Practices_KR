def solution(arr):
    answer = 0
    
    for i in range(len(arr)):
        answer += arr[i]
    
    answer /= len(arr)
    
    return answer