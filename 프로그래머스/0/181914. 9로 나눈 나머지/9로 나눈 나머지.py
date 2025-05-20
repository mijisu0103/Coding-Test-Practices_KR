def solution(number):
    answer = 0
    
    for i in number:
        i = int(i)
        answer += i
    
    while answer > 9:
        answer %= 9
    
    return answer