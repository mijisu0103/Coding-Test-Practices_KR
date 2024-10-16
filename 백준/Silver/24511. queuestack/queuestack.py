import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))

queue = deque([])
for i in range(n):
    if a[i] == 0:
        queue.append(b[i])
        
for i in range(l):
    queue.appendleft(c[i])
    print(queue.pop(), end=' ')