def solution(my_string, n):
    answer = ''
    lst = []
    
    for i in my_string:
        i *= n
        lst.append(i)
    
    return answer.join(lst)