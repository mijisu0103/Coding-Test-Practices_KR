import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

def gcd(a, b):
    while b:
        tmp = b
        b = a % b
        a = tmp
    return a

print(a*b//gcd(a, b))