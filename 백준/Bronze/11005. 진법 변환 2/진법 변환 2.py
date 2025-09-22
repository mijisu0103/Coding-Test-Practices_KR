from sys import stdin

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, stdin.readline().split())

result = ''

while n != 0:
    result += str(tmp[n%b])
    n = n//b

print(result[::-1])