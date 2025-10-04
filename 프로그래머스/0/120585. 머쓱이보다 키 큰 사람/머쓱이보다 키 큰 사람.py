def solution(array, height):
    answer = 0
    p = 0
    
    array.append(height)
    array = sorted(array)
    
    for i in range(len(array)):
        if array[i] <= height:
            continue
        answer += 1
    
    return answer