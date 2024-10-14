n = int(input())
result = 0

for i in range(n):
    a = list(map(int, str(i)))
    if n == sum(a) + i:
        result = i
        break;
print(result)