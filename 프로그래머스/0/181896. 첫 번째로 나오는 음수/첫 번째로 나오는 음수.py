def solution(num_list):
    answer = -1
    
    for i in num_list:
        if int(i) < 0:
            answer += num_list.index(i) + 1
            break
        else:
            continue
    
    return answer