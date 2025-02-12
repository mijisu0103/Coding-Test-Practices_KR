import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

queue = PriorityQueue()

for _ in range(n):
    num = int(input())
    if num == 0:
        if queue.empty():
            print(0)
        else:
            print(queue.get()[1])
    else:
        queue.put((abs(num), num))