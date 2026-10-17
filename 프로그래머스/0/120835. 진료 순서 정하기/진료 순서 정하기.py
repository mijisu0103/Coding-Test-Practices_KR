def solution(emergency):
    answer = []
    
    p = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(p.index(i) + 1)
    
    return answer