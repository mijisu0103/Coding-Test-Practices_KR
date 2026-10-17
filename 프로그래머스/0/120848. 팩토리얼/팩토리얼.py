from math import factorial

def solution(n):
    answer = 0

    while factorial(answer + 1) <= n:
        answer += 1

    return answer