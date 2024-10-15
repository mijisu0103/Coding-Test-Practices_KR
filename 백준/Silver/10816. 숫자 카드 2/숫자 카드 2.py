import sys
input = sys.stdin.readline

n = (int(input().strip()))
nl = list(map(int, input().strip().split()))

m = (int(input().strip()))
ml = list(map(int, input().strip().split()))

dict = {}

for n in nl:
    if n in dict:
        dict[n] += 1
    else: 
        dict[n] = 1

for m in ml:
    if m in dict:
        print(dict[m], end=' ')
    else:
        print(0, end=' ')