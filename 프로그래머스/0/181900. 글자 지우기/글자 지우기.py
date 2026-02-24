def solution(my_string, indices):
    answer = ''
    
    for i in range(0, len(my_string)):
        if i not in indices:
            answer += my_string[i]
        
    return answer