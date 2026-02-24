def solution(num_list, n):
    answer = []
    
    s = num_list[:n]
    e = num_list[n:]
    
    answer += e
    answer += s
    
    
    return answer