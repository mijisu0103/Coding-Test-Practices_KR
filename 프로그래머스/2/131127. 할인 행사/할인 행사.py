from collections import Counter

def solution(want, number, discount):

    check = len(discount) - 9
    days, start, end = 0, 0, 10
    
    for _ in range(check):

        days += 1
        counter = Counter(discount[start:end])
        
        for item, count in zip(want, number):
            if counter[item] != count:
                days -= 1
                break
        
        start += 1
        end += 1
    
    return days