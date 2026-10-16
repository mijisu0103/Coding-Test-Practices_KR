def solution(strArr):
    d = {}
    
    for s in strArr:
        if len(s) in d:
            d[len(s)] += 1
        else:
            d[len(s)] = 1
            
    return max(d.values())