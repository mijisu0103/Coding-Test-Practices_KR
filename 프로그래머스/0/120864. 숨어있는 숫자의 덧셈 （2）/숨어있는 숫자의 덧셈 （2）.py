def solution(my_string):
    
    for s in my_string:
        if s.isalpha() == True:
            my_string = my_string.replace(s, ' ')
    
    return sum(map(int, my_string.split()))