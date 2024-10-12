n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        min = max = a[i]
    else:
        if min > a[i]:
            min = a[i]
        if max < a[i]:
            max = a[i]
            
print(min, max)