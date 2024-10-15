import sys

cd = []

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    cd.append([y,x])

s_cd = sorted(cd)
    
for y, x in s_cd:
    print(x, y)
    