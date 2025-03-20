def solution(num_list):
    answer = 0
    multiple = 1
    mul_sum = 0
    
    for i in num_list:
        multiple *= i
        mul_sum += i
        mul_squared = mul_sum **2
    
    if multiple < mul_squared:
        answer = 1
    else:
        answer = 0
    
    return answer