import sys

input = sys.stdin.readline
n, m = map(int, input().split())

sum = [0]
sum += list(map(int, input().split()))

for i, num in enumerate(sum):
    if i > 0:
        sum[i] = sum[i - 1] + num

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])