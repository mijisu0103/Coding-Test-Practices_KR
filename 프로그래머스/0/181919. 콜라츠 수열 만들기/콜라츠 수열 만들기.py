def solution(n):
    answer = [n]

    while answer[-1] != 1:
        if answer[-1] % 2 == 0:
            answer.append(answer[-1]/2)
        else:
            answer.append(3*answer[-1]+1)
    
    return answer