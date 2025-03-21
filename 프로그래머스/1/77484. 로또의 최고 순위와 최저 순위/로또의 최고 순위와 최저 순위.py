def solution(lottos, win_nums):
    
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} 
    
    none = lottos.count(0) 
    equal = 0 
    for wn in win_nums: 
        if wn in lottos:
            equal += 1
    
    best = ranking[equal+none]
    lowest = ranking[equal]
    answer = [best, lowest]
    
    return answer