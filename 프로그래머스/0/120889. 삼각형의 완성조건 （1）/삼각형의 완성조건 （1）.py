def solution(sides):
    answer = 0
    
    longest = sides.pop(sides.index(max(sides)))
    
    sum = sides[0] + sides[1]
    
    if sum > longest:
        answer += 1
    else:
        answer += 2
    
    return answer