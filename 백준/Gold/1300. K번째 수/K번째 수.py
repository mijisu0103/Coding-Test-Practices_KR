import sys
input = sys.stdin.readline
def x_is_greater(low, high):
    x = (low + high) // 2
    cnt=0 
    same_cnt = 0 
    idx = n 
    for i in range(1, n + 1):
        while i * idx > x and idx >= 1: 
            idx -= 1
        if i * idx == x: 
            same_cnt += 1
        elif idx < 1:
            break
        cnt += idx 
    
    if cnt - same_cnt < k <= cnt: 
        print(x)
        exit()
    elif cnt - same_cnt >= k:
        x_is_greater(low, x - 1)
    else:
        x_is_greater(x + 1, high)
n = int(input()) 
k = int(input()) 

x_is_greater(1, n ** 2)