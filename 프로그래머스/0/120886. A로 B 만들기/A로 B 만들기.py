from collections import Counter

def solution(before, after):
    answer = 0
    
    b = Counter(before)
    a = Counter(after)
    
    return 1 if b == a else 0