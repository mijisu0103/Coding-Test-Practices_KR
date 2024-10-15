import sys

n = int(sys.stdin.readline())
p = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    p.append((x,y))

p.sort()

for i in range(n):
    print(p[i][0], p[i][1])
    