def solution(x):
    answer = True
    sum = 0
    
    X = list(str(x))
    
    for i in X:
        sum += int(i)
    
    if x % sum == 0:
        answer = True
    else:
        answer = False
    
    return answer