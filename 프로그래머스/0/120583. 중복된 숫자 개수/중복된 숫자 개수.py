def solution(array, n):
    answer = 0
    
    for i in array:
        if int(i) == n:
            answer += 1
    
    return answer