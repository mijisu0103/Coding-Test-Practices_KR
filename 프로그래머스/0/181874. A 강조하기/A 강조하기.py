def solution(myString):
    answer = ''
    
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += 'A'
        
        elif myString[i] != 'A' and myString[i].isupper() == True:
            answer += myString[i].lower()
        
        else:
            answer += myString[i]
    
    return answer