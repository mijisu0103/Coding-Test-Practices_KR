n = int(input())
m = int(input())

p = []
for x in range(n, m+1):
    np = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                np += 1
                break
        if np == 0:
            p.append(x)
            
if len(p) > 0:
    print(sum(p))
    print(min(p))
    
else:
    print(-1)

    