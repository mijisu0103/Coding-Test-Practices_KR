import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    print(a*b // gcd(a,b))
    
    