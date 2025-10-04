def solution(n, k):
    answer = 0
    cnt = 0
     
    cnt += 1 * (n // 10)
    
    answer += 12000 * n + 2000 * (k - cnt)
    
    return answer