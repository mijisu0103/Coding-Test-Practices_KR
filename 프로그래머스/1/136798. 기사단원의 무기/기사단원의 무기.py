def solution(number, limit, power):
    divs = []
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1
        
        if cnt > limit:
            divs.append(power)
        else:
            divs.append(divs) if False else divs.append(cnt)
            
    return sum(divs)