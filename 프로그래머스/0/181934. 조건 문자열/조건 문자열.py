def solution(ineq, eq, n, m):
    answer = 0
    
    if eq == "!":
        if ineq == "<":
            return int(n<m)
        else:
            return int(n>m)
    else:
        if ineq == "<":
            return int(n<=m)
        else:
            return int(n>=m)
    
    return answer