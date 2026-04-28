def solution(arr):
    
    cnt_0 = 0
    
    if len(arr) > len(arr[0]):
        cnt_0 += len(arr) - len(arr[0])
        
        for a in arr:
            a.extend([0] * cnt_0)
        
    elif len(arr) < len(arr[0]):
        cnt_0 += len(arr[0]) - len(arr)
        
        for _ in range(cnt_0):
            arr.append([0] * len(arr[0])) 
    
    return arr