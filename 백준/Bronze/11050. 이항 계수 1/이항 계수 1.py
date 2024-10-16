def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)

n, k = map(int, input().split())
print(fac(n) // (fac(k) * fac(n-k)))