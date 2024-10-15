n, m = map(int, input().split())

s = set()
cnt = 0

for i in range(n):
    s.add(input())
    
for i in range(m):
    test = input()
    if test in s:
        cnt +=1

print(cnt)