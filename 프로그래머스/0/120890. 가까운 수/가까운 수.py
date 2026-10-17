def solution(array, n):
    number = []
    array = sorted(array)
    
    for i in array:
        number.append(abs(i-n))
        
    return array[number.index(min(number))]