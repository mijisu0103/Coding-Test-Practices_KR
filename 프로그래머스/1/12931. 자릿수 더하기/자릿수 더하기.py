def solution(n):
    new = str(n)
    add = 0
    
    for i in range(len(new)):
        add += int(new[i])
        
    return add