K, N = map(int, input().split())

lans = []

for i in range(K):
    lan = int(input())
    lans.append(lan)

min_length, max_length = 1, max(lans)

while min_length <= max_length:
    mid = (min_length + max_length) // 2
    lines = 0

    for i in lans:
        lines += i // mid

    if lines >= N:
        min_length = mid + 1

    else:
        max_length = mid - 1

print(max_length)