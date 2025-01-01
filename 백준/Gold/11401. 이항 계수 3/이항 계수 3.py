import sys

N, K = map(int, sys.stdin.readline().split())
p = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % p

    return result

def col(n, k):
    if (k == 0):
        return 1
    
    if (k == 1):
        return n
    
    result = col(n, k // 2)
    if (k % 2 == 0):
        return result * result % p
    else:
        return result * result * n % p

top = factorial(N)
bottom = factorial(N - K) * factorial(K) % p
answer = top * col(bottom, p - 2) % p
print(answer)