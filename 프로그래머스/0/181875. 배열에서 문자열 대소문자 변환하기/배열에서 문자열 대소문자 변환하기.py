def solution(strArr):
    
    answer = []
    
    for idx, i in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
            
    return answer