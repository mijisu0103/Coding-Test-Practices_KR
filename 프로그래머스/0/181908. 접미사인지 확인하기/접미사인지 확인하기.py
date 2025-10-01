def solution(my_string, is_suffix):
    answer = 0
    
    
    if is_suffix in [my_string[i:] for i in range(len(my_string))]:
        answer += 1
    
    return answer