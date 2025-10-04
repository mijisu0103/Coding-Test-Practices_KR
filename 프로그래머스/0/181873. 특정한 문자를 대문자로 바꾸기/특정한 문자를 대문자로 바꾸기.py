def solution(my_string, alp):
    
    return ''.join([char.upper() if char == alp else char for char in my_string])