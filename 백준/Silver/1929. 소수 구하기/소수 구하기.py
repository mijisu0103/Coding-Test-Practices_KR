import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if isPrime(i):
        print(i)