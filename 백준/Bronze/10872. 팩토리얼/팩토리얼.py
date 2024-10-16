def fac(n):
    ans = 1
    if n>0:
        ans = n * fac(n-1)
    return ans

n = int(input())
print(fac(n))