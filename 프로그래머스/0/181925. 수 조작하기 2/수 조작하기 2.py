def solution(numLog):
    answer = []
    
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            answer.append('w')
        elif numLog[i] - numLog[i-1] == -1:
            answer.append('s')
        elif numLog[i] - numLog[i-1] == 10:
            answer.append('d')        
        else:
            answer.append('a')      
    return ''.join(answer)