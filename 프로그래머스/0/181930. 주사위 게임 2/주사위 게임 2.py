def solution(a, b, c):
    answer = a+b+c
    
    if a==b and b==c and a==c:
        for i in range(2, 4):
            answer *= (a**i + b**i + c**i)
    elif a!=b and b!=c and a!=c:
        answer = answer
    else:
        for i in range(2, 3):
            answer *= (a**i + b**i + c**i)
    
    return answer