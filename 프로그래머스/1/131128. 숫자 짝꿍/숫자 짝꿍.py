from collections import Counter

def solution(X, Y):
    temp = []
    x, y = Counter(X), Counter(Y)
    pair = x & y
    
    for p in pair:
        temp.append(p * pair[p])
    
    answer = ''.join(sorted(temp, reverse=True))

    return '-1' if not answer else '0' if answer[0] == '0' else answer