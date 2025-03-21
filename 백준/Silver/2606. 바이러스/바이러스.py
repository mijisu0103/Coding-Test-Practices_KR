import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

net = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

def bfs():
    q = deque()
    count = 0
    q.append(1)
    
    visited[1] = True
    
    while q:
        cur = q.popleft()
        
        for i, val in enumerate(net[cur]):
            if visited[val] == False:
                q.append(val)
                visited[val] = True
                count += 1
    print(count)
    
visited = [False for _ in range(N + 1)]

bfs()