def solution(my_string):
    answer = ''
    seen = set()
    
    for i in range(len(my_string)):
        if my_string[i] not in seen:
            seen.add(my_string[i])
            answer += my_string[i]
    
    return answer