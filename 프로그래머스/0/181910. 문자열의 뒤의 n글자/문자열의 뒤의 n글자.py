def solution(my_string, n):
    answer = []
    
    for i in range(n):
        answer.append(my_string[-i-1])
    
    return ''.join(answer[-1::-1])