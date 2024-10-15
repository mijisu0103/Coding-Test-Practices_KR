import sys

input = sys.stdin.readline

n = int(input())
l = set(map(int, input().split()))

m = int(input())
ml = list(map(int, input().split()))

for i in range(m):
    if ml[i] in l:
        print(1, end=" ")
    else:
        print(0, end=" ")