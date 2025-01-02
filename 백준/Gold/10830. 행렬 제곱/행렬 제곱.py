def multi(a, b):
    X = [[0] * N for _ in range(N)]
    for i in range(N): 
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k] * b[k][j] % 1000 
    return X

def square(x, n): 
    if n == 1:
        return x
    temp = square(x, n//2)
    if n % 2 == 0 :
        return multi(temp, temp)
    else : 
        return multi(multi(temp, temp), x)

import sys
N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = square(A, B)
for i in range(N):
    for j in range(N):
        result[i][j] = result[i][j] % 1000

for k in result:
    print(*k)