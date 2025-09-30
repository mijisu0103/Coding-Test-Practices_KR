N = int(input())
parent = list(map(int, input().split()))
R = int(input())

for i in range(N):
    if parent[i] == -1:
        root = i
        break
    
black = [0] * N
for i in range(N):
    u = i
    while True:
        if u == R:
            black[i] = 1
            break
            
        if u == root:
            break
        
        u = parent[u]
        
red = [0] * N
for i in range(N):
    if black[i] == 1:
        continue
    
    if i == root:
        continue
        
    red[parent[i]] = 1
    
count = 0
for i in range(N):
    if black[i] == 1 or red[i] == 1:
        continue
    count += 1
    
print(count)