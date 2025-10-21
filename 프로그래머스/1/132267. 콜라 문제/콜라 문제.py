def solution(a, b, n):
    
    coke = 0
    
    while n >= a:
        
        newCount = n // a * b
        leftover = n % a

        coke += newCount
        n = leftover + newCount
    
    return coke