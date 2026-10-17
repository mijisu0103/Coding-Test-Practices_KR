from collections import Counter

def solution(s):
    answer = ''
    s_cnt = Counter(s)
    
    for i in s_cnt:
        if s_cnt[i] == 1:
            answer += i
    
    answer = ''.join(sorted(answer))
    
    return answer