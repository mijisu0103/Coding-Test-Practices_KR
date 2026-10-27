def solution(data, ext, val_ext, sort_by):
    answer = []
    col = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    for c in data:
        if c[col[ext]] < val_ext:
            answer.append(c)
    
    return sorted(answer, key=lambda x: x[col[sort_by]])