n = int(input())

num, cnt = 1, 1

while n > num:
    num += 6 * cnt
    cnt += 1
print(cnt)