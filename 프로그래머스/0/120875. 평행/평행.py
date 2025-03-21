from itertools import combinations

def solution(dots):
    answer = 0
    
    combi = list(combinations(dots, 2)) 
    
    for i in range(len(combi)//2): 
        dx1, dy1 = combi[i][0][0] - combi[i][1][0], combi[i][0][1]-combi[i][1][1]
        dx2, dy2 = combi[-(i+1)][0][0]-combi[-(i+1)][1][0], combi[-(i+1)][0][1]-combi[-(i+1)][1][1]
        d1 = dy1/dx1 
        d2 = dy2/dx2 
        
        if d1 == d2: 
            answer = 1
            break
        answer = 0 

    return answer