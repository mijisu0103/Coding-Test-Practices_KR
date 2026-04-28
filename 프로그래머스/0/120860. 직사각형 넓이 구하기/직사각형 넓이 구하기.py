def solution(dots):
    
    xs, ys = set(), set()
    
    for x, y in dots:
        xs.add(x)
        ys.add(y)
    
    return (max(xs) - min(xs)) * (max(ys) - min(ys))