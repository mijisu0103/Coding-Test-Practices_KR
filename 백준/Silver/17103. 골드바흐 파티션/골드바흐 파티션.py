import sys
input = sys.stdin.readline

arr = [1] * 1000002
arr[:2] = 0, 0
p = []

for i in range(2, 1000002):
    if arr[i]:
        p.append(i)
        for j in range(i*i, 1000002, i):
            arr[j] = 0
            
n = int(input())

for _ in range(n):
    cnt = 0
    m = int(input())
    for k in p:
        if k >= m:
            break
        if arr[m-k] and k<= m-k:
            cnt += 1
    print(cnt)