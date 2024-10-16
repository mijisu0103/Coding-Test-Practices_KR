from itertools import combinations
n, k = map(int, input().split())
l = [i for i in range(n)]
print(len(list(combinations(l, k))))