n = int(input())

a = list(map(int, input().split()))

max = 0
for i in range(n):
    if max < a[i]:
        max = a[i]
        
sum = 0.0
for i in range(n):
    sum = sum + a[i]/max*100

print(sum/n)