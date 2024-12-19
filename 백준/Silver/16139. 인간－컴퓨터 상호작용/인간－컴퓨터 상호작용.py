import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

count = [[0] * 26]
for i in range(len(S)):
    count.append(count[len(count) - 1][:])
    count[i + 1][ord(S[i]) - 97] += 1

for _ in range(q):
    a, l, r = map(str, sys.stdin.readline().split())
    result = count[int(r) + 1][ord(a) - 97] - count[int(l)][ord(a) - 97]
    print(result)