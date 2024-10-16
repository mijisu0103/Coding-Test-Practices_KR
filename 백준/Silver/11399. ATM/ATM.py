n = int(input())
p = list(map(int, input().split()))

p.sort()
ans = 0

for x in range(1, n+1):
    ans += sum(p[0:x])
print(ans)