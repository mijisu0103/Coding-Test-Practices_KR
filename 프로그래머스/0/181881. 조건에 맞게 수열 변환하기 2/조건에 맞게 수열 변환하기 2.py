def solution(arr):
    cnt = 0
    
    while True:
        prev_arr = arr[:]
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
                
        if prev_arr == arr:
            break
            
        cnt += 1
        
    return cnt