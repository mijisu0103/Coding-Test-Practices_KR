import math

m = 123456

array1 = [True for _ in range(2 * m + 1)]
array1[0], array1[1] = False, False

for i in range(2, int(math.sqrt(2 * m) + 1)):
    if array1[i]:
        j = 2
        while i * j <= 2 * m:
            array1[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0: #0이면 반복문 탈출
        break

    count = 0

    for i in range(n+1, 2 * n + 1):
        if array1[i]:
            count += 1
    print(count)