import sys
input = sys.stdin.readline

t = input().rstrip()
s = set()

for i in range(len(t)):
    for j in range(i, len(t)):
        tmp = t[i:j+1]
        s.add(tmp)
        
print(len(s))