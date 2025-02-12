import sys
from queue import PriorityQueue

input = sys.stdin.readline
queue= PriorityQueue()

N = int(input())

for _ in range(N):
    n = int(input())
    if(n == 0):
        if queue.empty():
            print('0')
            continue
        print(queue.get())
    else:
        queue.put(n)