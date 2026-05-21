def solution(picture, k):
    answer = []
    
    for p in picture:
        char = ""
        
        for l in p:
            char += l * k
        
        for count in range(k):
            answer.append(char)
    
    return answer