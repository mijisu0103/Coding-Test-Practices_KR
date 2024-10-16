import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
wl = {}

for _ in range(n):
    word = input().rstrip()
    
    if len(word) < m:
        continue
    else:
        if word in wl:
            wl[word] += 1
        else:
            wl[word] = 1

wl = sorted(wl.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in wl:
    print(i[0])