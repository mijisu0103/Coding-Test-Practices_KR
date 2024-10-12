h, m = map(int, input().split())

cooking_time = int(input())

hm = h * 60 + m
hm += cooking_time

print((hm // 60) % 24, hm % 60)