def solution(money):
    answer = []
    
    max_a = money // 5500
    change = money - 5500 * max_a
    
    answer.append(max_a)
    answer.append(change)
    
    return answer