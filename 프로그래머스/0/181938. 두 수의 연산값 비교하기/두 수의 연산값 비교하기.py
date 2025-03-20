def solution(a, b):
    answer = 0
    
    double_ab = 2 * a * b
    ab = int(str(a) + str(b))
    
    if double_ab > ab:
        answer = double_ab
    else:
        answer = ab
    
    return answer