import sys
from collections import deque

input = sys.stdin.readline

arr = deque()

for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        arr.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)