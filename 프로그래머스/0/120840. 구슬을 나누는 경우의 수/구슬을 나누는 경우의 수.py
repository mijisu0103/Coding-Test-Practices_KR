from math import factorial

def solution(balls, share):
    
    ans = factorial(balls) / (factorial(balls - share) * factorial(share))
    
    return ans