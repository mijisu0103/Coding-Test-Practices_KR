def solution(n):
    answer = 0
    check = {}
    
    check[1] = 1
    check[2] = 2
    
    for i in range(3, n + 1):
        check[i] = check[i - 1] + check[i - 2]
    
    answer = check[n] % 1234567
    
    return answer