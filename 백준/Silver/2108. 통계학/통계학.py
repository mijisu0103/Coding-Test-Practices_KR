import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

avg = round(sum(arr)/n)
print(avg)

arr.sort()
mid = n//2
print(arr[mid])

mode = Counter(arr).most_common()
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
    
k = max(arr) - min(arr)
print(k)