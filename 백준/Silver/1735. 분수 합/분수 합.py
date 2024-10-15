import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())   
c, d = map(int, input().rstrip().split())

e = a * d + b * c
f = b * d

def gcd(e, f):
    while f:
        e, f = f, e % f
    return e

print(e//gcd(e, f), f//gcd(e, f))