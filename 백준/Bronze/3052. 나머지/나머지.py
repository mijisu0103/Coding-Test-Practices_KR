a = [0]*42

for i in range(10):
    v = int(input())
    a[v%42] = 1
    
count = 0
for i in range(42):
    if a[i] == 1:
        count += 1
        
print(count)