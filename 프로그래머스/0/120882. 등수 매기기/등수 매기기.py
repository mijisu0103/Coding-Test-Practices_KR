def solution(score):
    
    avg = [ ( s[0] + s[1] ) / 2 for s in score]
    sorted_avg = sorted(avg, reverse = True)
    answer = [ sorted_avg.index(a) + 1 for a in avg ]
    
    return answer