def solution(num, k):
    
    num = str(num)
    
    for idx, ch in enumerate(num):
        if ch == str(k):
            return idx + 1
        
    return -1
