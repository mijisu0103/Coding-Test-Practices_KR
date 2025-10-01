def solution(my_string, is_prefix):
    answer = 0
    
    if is_prefix in [my_string[:i+1] for i in range(len(my_string))]:
        answer += 1
    
    return answer