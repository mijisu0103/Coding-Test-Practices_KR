N = int(input())

sum = 0

for i in range(1, N+1):
    sum += (N//i) * i

print(sum)