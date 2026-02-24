def solution(arr, intervals):
    answer = []
    
    for i, (s,e) in enumerate(intervals):
        answer += arr[s:e+1]
    
    return answer