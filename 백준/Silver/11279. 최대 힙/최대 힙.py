import sys
from queue import PriorityQueue
input = sys.stdin.readline
queue = PriorityQueue() 

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if queue.empty():
            print('0')
            continue
        print(abs(queue.get()))  
    else:
        queue.put(-x) 