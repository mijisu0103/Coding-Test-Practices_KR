def solution(my_string):
    
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i not in vowels:
            answer += i
 
    return answer