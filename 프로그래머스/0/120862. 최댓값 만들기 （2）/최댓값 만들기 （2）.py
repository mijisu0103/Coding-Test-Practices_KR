import itertools

def solution(numbers):
    answer = []
    
    for x, y in itertools.combinations(numbers, 2):
        answer.append(x*y)
        
    return max(answer)